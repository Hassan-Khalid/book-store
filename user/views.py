from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView, CreateView


# Create your views here.

class MainPage(TemplateView):
    template_name = 'user/index.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
