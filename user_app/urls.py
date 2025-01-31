from django.urls import path
from . import views
from . views import RegisterView

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
