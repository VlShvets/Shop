from django.contrib import admin

# Register your models here.
from page.models import Category, Good, BlogArticle

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(BlogArticle)
