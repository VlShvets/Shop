from django.conf.urls import url
from page import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^(?:(?P<cat_id>\d+)/){1}$', views.category, name = "category"),
    url(r'^good/$', views.goods, name = "goods"),
    url(r'^good/(?:(?P<good_id>\d+)/){1}$', views.good, name = "good"),
]
