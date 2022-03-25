from django.urls import path

from mainapp import views


urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.products, name="products"),
    path('contacts/', views.contacts, name="contacts"),
]
