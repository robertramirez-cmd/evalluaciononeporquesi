from django.contrib import admin
from django.urls import path
from app_uno import views as views_uno
from app_dos import views as views_dos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista1/', views_uno.primera_vista, name='vista1'),
    path('vista2/', views_uno.segunda_vista, name='vista2'),
    path('vista3/', views_dos.tercera_vista, name='vista3'),
    path('vista4/', views_dos.cuarta_vista, name='vista4'),
]