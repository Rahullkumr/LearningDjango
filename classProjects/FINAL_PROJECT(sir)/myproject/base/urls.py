
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('remove/<int:pk>',views.remove,name='remove'),
]