from django.urls import path
 
from . import views

app_name = 'login_app'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
]