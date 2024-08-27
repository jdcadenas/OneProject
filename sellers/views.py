from django.shortcuts import render

from .models import Seller


def show_seller(request):
    print('aqui')
    return render(request, "sellers/list.html",{'sellers': Seller.get_annotated_list()})




# end def
