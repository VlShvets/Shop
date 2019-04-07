from django.shortcuts import render

from page.models import Category, Good
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def index(request):
    cats = Category.objects.all()
    s = "Категории: " + "<br><br>"
    for cat in cats:
        s = s + cat.name + "<br><br>"
       
    return HttpResponse(s)

def category(request, cat_id):
    if cat_id == None:
        cat = Category.objects.first()
    else:
        try:
            cat = Category.objects.get(pk = cat_id)
        except:
            raise Http404

    goods = Good.objects.filter(category = cat).order_by("name")
    s = "Категория: " + cat.name + "<br><br>"
    
    for good in goods:
        s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
        
    return HttpResponse(s)
   
def goods(request):
    goods = Good.objects.all()
    s = "Товары:" + "<br><br>"
    for good in goods:
        s = s + good.name + "<br>" + good.category.name + "<br>" + good.description + "<br>"
    
        if not good.in_stock:
            s = s + "Нет в наличии!"
            
        s = s + "<br><br>"

    return HttpResponse(s)
   
def good(request, good_id):
    if good_id == None:
        good = Good.objects.first()
    else:
        try:
            good = Good.objects.get(pk = good_id)
        except Good.DoesNotExist:
            raise Http404

    s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description
    
    if not good.in_stock:
        s = s + "<br><br>" + "Нет в наличии!"

    return HttpResponse(s)
