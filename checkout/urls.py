from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('make_purchase/<order_number>', views.make_purchase, name='make_purchase'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
