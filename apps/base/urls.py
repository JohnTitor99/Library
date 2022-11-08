from django.urls import path, include
from .views import LibrariesList, LoginPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('library/', include('apps.library_app.urls')),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', LibrariesList.as_view(), name='libraries'),
]