from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(AdType)
admin.site.register(AdCategory)
admin.site.register(AdImage)
admin.site.register(AdCard)
