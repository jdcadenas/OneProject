from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import CategoryMenu


class CategoryMenuAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(CategoryMenu, MPTTModelAdmin)
