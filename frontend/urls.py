
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'frontend'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>',
         views.category_list, name='category_list')
]
