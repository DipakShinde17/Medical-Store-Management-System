from django.contrib import admin
from .models import Medicine,Supplier
from .models import StoreProfile
from .models import Settings

admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(StoreProfile)
admin.site.register(Settings)