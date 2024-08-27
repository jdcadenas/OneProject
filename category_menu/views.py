from django.shortcuts import render

from category_menu.models import CategoryMenu


def show_category_menu(request):
    return render(request,"category_menu/list.html",{'category_menu': CategoryMenu.objects.all()})
