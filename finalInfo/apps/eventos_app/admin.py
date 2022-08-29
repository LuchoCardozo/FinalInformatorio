# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Evento




class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'organizador', 'img')
    search_fields = ('nombre', 'organizador', 'creado')
    list_per_page = 25

    readonly_fields = ['evento_img']

    def evento_img(self,obj):
        return mark_safe('<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url))

admin.site.register(Evento, EventoAdmin)
