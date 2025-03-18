from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('',views.home ,name="home"),
    path('reg/',views.regis,name="reg"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('thanks/',views.thank_page,name="thanks"),
    path('cart/',views.cart_page,name="cart"),
    path('vieworders/',views.vieworders_page,name="vieworders"),
    path("checkout/", views.checkout, name="checkout"),
    path("order/<int:order_id>/", views.order_details, name="order_details"),
    path('update-order-status/<int:order_id>/', update_order_status, name='update_order_status'),
    path('fav_viewpage/',views.fav_viewpage,name="fav_viewpage"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('collection/',views.collect,name="collect"),
    path('collection/<str:fname>',views.collections,name="collections"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),#Don't give the backslash because post method cannot take the slash
    path('fav',views.fav_page,name="fav"),
    path('address/', address_page, name='address_page'),
    path("payment/", payment_page, name="payment_page"),
    path("process_payment/", process_payment, name="process_payment"),
    path("create_order/", create_order, name="create_order"),
     path("cod_order/", cod_order, name="cod_order"),
]