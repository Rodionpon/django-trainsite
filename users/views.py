from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import CustomUser

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("main:dashboard")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
