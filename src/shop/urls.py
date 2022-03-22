from django.contrib import admin
from django.urls import path

from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="home"),
    path('products/', views.products, name="products"),
    path('contacts/', views.contacts, name="contacts"),
]

