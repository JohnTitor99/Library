from django.urls import path
from .views import WishCreate, WishUpdate

urlpatterns = [
    path('create/<str:lib_name>/', WishCreate.as_view(), name='wish_create'),
    path('update/<str:lib_name>/<int:pk>/', WishUpdate.as_view(), name='wish_update'),
]