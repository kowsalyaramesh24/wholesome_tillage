from django.contrib import admin
from .models import adminpanel,adminfruits,admingreens,admintubers,adminveg,soil,Red,Black,Alluvial,Sandy,Clay

# Register your models here.
admin.site.register(adminpanel)
admin.site.register(adminfruits)
admin.site.register(adminveg)
admin.site.register(admintubers)
admin.site.register(admingreens)
admin.site.register(soil)
admin.site.register(Red)
admin.site.register(Black)
admin.site.register(Alluvial)
admin.site.register(Sandy)
admin.site.register(Clay)
