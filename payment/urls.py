from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.CartView, name='cart'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
    path('payment_option/', views.payment_option, name='payment_option')
]