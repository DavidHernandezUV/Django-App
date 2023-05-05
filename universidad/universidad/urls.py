from django.contrib import admin
from django.urls import path
from Academic.views import formulario_contacto, contactar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactForm/', formulario_contacto),
    path('contactSuccessfully/', contactar)
]
