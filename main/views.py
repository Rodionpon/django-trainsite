from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from .models import TrainingProdram, Training
# Create your views here.

# @login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def trainings(request):
    return render(request, 'trainings.html')

class TrainingListView(ListView):
    model = Training
    template_name = "trainings.html"
    context_object_name = "trainings"

    def get_queryset(self):
        return Training.objects.all()
    
class TrainingCreateView(CreateView):
    model = Training
    template_name = "create_training.html"
    fields = ["title","description","image"]
    success_url = reverse_lazy("main:trainings")