from django.shortcuts import render

from page.models import Category, Good
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def index(request):
    cats = Category.objects.all().order_by("name")
           
    return render(request, "index.html", { "cats": cats })

def category(request, cat_id):
    cats = Category.objects.all().order_by("name")
    try:
        cat = Category.objects.get(pk = cat_id)
    except:
        raise Http404

    goods = Good.objects.filter(category = cat).order_by("name")
        
    return render(request, "index.html", { "category": cat, "cats": cats, "goods": goods})
   
def goods(request):
    cats = Category.objects.all().order_by("name")
    goods = Good.objects.all().order_by("name")

    return render(request, "index.html", { "cats": cats, "goods": goods})
   
def good(request, good_id):
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk = good_id)
    except Good.DoesNotExist:
        raise Http404

    return render(request, "good.html", { "cats": cats, "good": good})
