from smtplib import SMTPException
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactContent
from django.conf import settings
import requests
import lesfilmsdeole.settings


@require_http_methods(['POST'])
def contact(request):
    if not request.is_ajax():
        raise Http404

    form = ContactForm(request.POST or None)
    if not form.is_valid():
        return JsonResponse({"error": "fields"}, status=422)

    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    recaptcha_response = form.data['g-recaptcha-response']

    request = requests.post('https://www.google.com/recaptcha/api/siteverify',
                            data={
                                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                                'response': recaptcha_response
                            })
    result = request.json()

    if not result['success']:
        return JsonResponse({"error": "captcha"}, status=422)

    response = requests.post(
        settings.EMAIL_URL,
        auth=("api", settings.EMAIL_API_KEY),
        data={"from": "{0} <{1}>".format(name, email),
              "to": ["Les Films d'Éole <{0}>".format(ContactContent.objects.last().email)],
              "subject": subject,
              "text": render_to_string("contact/email.html", {"message": message})})

    if response.status_code == 200:
        return JsonResponse({"success": "success", "message": "Message envoyé!"})
    else:
        return JsonResponse({"error": "email"}, status=422)
