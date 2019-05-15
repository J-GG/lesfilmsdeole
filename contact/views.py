from smtplib import SMTPException
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import ContactContent
from django.conf import settings
import requests


@require_http_methods(['POST'])
def contact(request):
    if not request.is_ajax():
        raise Http404

    form = ContactForm(request.POST or None)
    if not form.is_valid():
        message = [input_message for input_message in form.errors]
        return JsonResponse({"error": "fields", "messages": message}, status=422)

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
        return JsonResponse({"error": "fields", "messages": {"recaptcha": "La vérification humaine est invalide"}},
                            status=422)

    msg = EmailMessage(subject=subject,
                       body=message,
                       from_email="{0} <{1}>".format(name, email),
                       to=["Les Films d'Éole <{0}>".format(ContactContent.objects.last().email)])
    try:
        msg.send()
    except SMTPException:
        return JsonResponse({"error": "mail",
                             "message": "Erreur lors de l'envoi du message. Réessayer plus tard ou contactez nous par email ou par téléphone."},
                            status=422)

    return JsonResponse({"success": "success", "message": "Message envoyé!"})
