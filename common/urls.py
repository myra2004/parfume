from django.urls import path

from .views import HomePageView, ContactPageView, ShopDetailsView, ShopCart


app_name = 'common'

urlpatterns = [
    path('index/', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('shop-details/<int:pk>/', ShopDetailsView.as_view(), name='shop-details'),
    path('shop-cart/', ShopCart.as_view(), name='shop-cart'),
]