from django.contrib import admin

from .models import Library, Wish, Finished, UserProfile

# Register your models here.

admin.site.register(Library)
admin.site.register(Wish)
admin.site.register(Finished)
admin.site.register(UserProfile)