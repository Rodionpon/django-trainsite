from django.urls import path 
from .views import dashboard, trainings, TrainingListView, TrainingCreateView


app_name = "main"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("trainigs/", TrainingListView.as_view(), name="trainings"),
    path("create_training/", TrainingCreateView.as_view(), name="create_treaning")
]
