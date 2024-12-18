from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    path('auth/', views.LoginUserView.as_view(), name='login_page'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile_pg'),
    path('password-change/', views.UserPassChangeView.as_view(), name='pass_change'),
    path('logout/', LogoutView.as_view(), name='logout')
]