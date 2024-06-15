from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard', views.leaderboard_view, name='leaderboard'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('message/<int:id>', views.message_view, name='message'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('terms_and_conditions', views.terms_conditions_view, name='terms_conditions'),
    path('search/users', views.search_users_view, name='search_users'),
]
