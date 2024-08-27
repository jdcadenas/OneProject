from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Seller


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Seller)


admin.site.register(Seller, MyAdmin)
