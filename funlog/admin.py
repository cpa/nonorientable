from funlog.models import Funfact
from django.contrib import admin

class FunfactAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Funfact, FunfactAdmin)
            
