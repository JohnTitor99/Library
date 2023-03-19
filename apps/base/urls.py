from django.urls import path, include
from .views import LibrariesList, LoginPage, LibrarySearch, RegisterPage, EditProfile, PasswordChange
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('library/', include('apps.library_app.urls')),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),
    path('password/', PasswordChange.as_view(), name='change_password'),
    path('lib-search/', LibrarySearch.as_view(), name='lib_search'),
    path('', LibrariesList.as_view(), name='libraries'),
]