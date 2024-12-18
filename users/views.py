from .forms import *
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class LoginUserView(LoginView):
    template_name = 'users/auth.html'
    form_class = LoginUserForm

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('index')


class UserPassChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    form_class = PassChangeForm
    success_url = reverse_lazy('index')
