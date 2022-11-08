from django.urls import path, include
from .views import FinishedCreate, FinishedUpdate

urlpatterns = [
    path('create/<str:lib_name>/', FinishedCreate.as_view(), name='finished_create'),
    path('update/<str:lib_name>/<int:pk>/', FinishedUpdate.as_view(), name='finished_update'),
]