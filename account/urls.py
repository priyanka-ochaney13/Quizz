from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('delete', views.deleteProfile, name='delete_profile'),
    path('settings', views.editProfile, name='edit_profile'),

]
