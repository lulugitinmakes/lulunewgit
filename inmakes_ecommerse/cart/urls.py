from django.urls import path
app_name='cart'
from cart import views

urlpatterns = [
    path('cart_id/',views._cart_id,name='_cart_id'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('cart_remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
    ]