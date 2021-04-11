from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login1, name='login'),
    path('logout/', views.logout1, name='logout'),
    path('profile/', views.show_profile, name='show_profile'),
    path('change/profile/', views.profile_edit, name='edit_profile'),
    path('change/password', views.change_password, name='change_password'),
    path('signup/', views.signup, name='signup')
]
