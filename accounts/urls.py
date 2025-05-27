from django.urls import path

from accounts.api_endpoints import (
    CartItemListAPIView,
)


urlpatterns = [
    path('cart-items/', CartItemListAPIView.as_view(), name='cart-items'),
]