from django.contrib import admin
from .models import signup,ads,releases,discover,features,add

# Register your models here.
admin.site.register(signup)
admin.site.register(ads)
admin.site.register(releases)
admin.site.register(discover)
admin.site.register(features)
admin.site.register(add)

