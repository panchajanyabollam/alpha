from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-user/', views.create_user, name='create_user')
]