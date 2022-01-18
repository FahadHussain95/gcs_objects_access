from allauth.socialaccount.models import SocialToken, SocialApp
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.http import JsonResponse


def get_bucket_data(request):
    if request.user.is_authenticated:
        token = SocialToken.objects.get(account__user=request.user, account__provider='google')
        credentials = Credentials(
            token=token.token,
            refresh_token=token.token_secret,
            token_uri='https://oauth2.googleapis.com/token',
            client_id='<client_id>',
            client_secret='<client_secret_key>'
        )

        service = build('storage', 'v1', credentials=credentials)
        req = service.objects().list(bucket='<bucket_name>')
        resp = req.execute()

        if service:
            return JsonResponse("Successful", {"service": resp})
        else:
            return JsonResponse("Unsuccessful", safe=False)
    else:

        return JsonResponse("User not verified", safe=False)
