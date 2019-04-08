from django.shortcuts import render

from page.models import Category, Good
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404


# Create your views here.
def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
        
    cats = Category.objects.all().order_by("name")
     
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = cat_id)
    
    paginator = Paginator(Good.objects.filter(category = cat).order_by("name"), 1)
        
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
        
    return render(request, "index.html", { "category": cat, "cats": cats, "goods": goods})
   
def good(request, good_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
        
    cats = Category.objects.all().order_by("name")
    
    try:
        good = Good.objects.get(pk = good_id)
    except Good.DoesNotExist:
        raise Http404;

    return render(request, "good.html", { "cats": cats, "good": good, "pn": page_num})
