from django.contrib import admin
from .models import MenuCase


class MenuCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'menu_name')
    list_filter = ('menu_name',)


admin.site.register(MenuCase, MenuCaseAdmin)
