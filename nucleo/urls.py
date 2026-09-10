from django.contrib import admin
from django.urls import path
from app_uno import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista1/', views.primera_vista, name='vista1'),
    path('vista2/', views.segunda_vista, name='vista2'),
]