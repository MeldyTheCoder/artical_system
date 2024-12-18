from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Rims)
admin.site.register(Categories)
admin.site.register(Spares)
admin.site.register(Order)