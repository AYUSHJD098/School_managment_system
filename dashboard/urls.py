
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create-student', views.create_student, name="create_student__form"),
]
