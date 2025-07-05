from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from firebase_admin import auth as firebase_auth
from django.contrib.auth.models import User
import json

@csrf_exempt  # ✅ Disable CSRF protection for this view
def firebase_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    body = json.loads(request.body.decode('utf-8'))
    id_token = body.get('idToken')

    if not id_token:
        return JsonResponse({'error': 'Missing ID token'}, status=400)

    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token.get('email', '')

        # Create or get Django user
        user, created = User.objects.get_or_create(username=uid, defaults={'email': email})
        
        if created:
            user.set_unusable_password()
            user.save()

        return JsonResponse({'status': 'success', 'uid': uid, 'email': email})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=401)
