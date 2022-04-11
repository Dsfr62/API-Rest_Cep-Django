from django.contrib import admin
from core.models import loc

# Register your models here.

class CepAdmin(admin.ModelAdmin):
    list_display = ('cep', 'bairro', 'data_criacao')
    list_filter = ('bairro',)

admin.site.register(loc, CepAdmin)