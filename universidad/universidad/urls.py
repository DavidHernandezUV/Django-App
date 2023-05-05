from django.contrib import admin
from django.urls import path
from Academic.views import formularioContacto, contactar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactForm/', formularioContacto),
    path('contactSuccessfully/', contactar)
]
