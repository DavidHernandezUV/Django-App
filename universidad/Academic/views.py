from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def formularioContacto(request):
    return render(request, "contactForm.html")


def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + \
            " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["jose.david.barona@correounivalle.edu.co"]
        send_mail(asunto, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "contactSuccessfully.html")
    return render(request, "contactForm.html")
