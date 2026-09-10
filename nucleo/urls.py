from django.contrib import admin
from django.urls import path
from app_dos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista3/', views.tercera_vista, name='vista3'),
    path('vista4/', views.cuarta_vista, name='vista4'),
]