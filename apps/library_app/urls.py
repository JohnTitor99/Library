from django.urls import path, include
from .views import LibraryOpen, LibraryCreate, LibraryDelete, LibraryUpdate

urlpatterns = [
    path('wish_list/', include('apps.wish_list_app.urls')),
    path('shelf/', include('apps.shelf_app.urls')),

    path('create/', LibraryCreate.as_view(), name='library_create'),
    path('delete/<int:pk>/', LibraryDelete.as_view(), name='library_delete'),
    path('update/<int:pk>/', LibraryUpdate.as_view(), name='library_update'),
    path('<str:lib_name>/', LibraryOpen.as_view(), name='library_open'),
]