from django.contrib import admin
from .models import customUser,Patient,Doctor,BlogPost
#
# Register your models here.
admin.site.register(customUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(BlogPost)
# admin.site.register(BlogCategory)
