from django.urls import path

from products.api_endpoints import *

urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name='product-list1'),
    path('list2/', ProductListAPIView2.as_view(), name='product-list2'),
    path('list3/', ProductListAPIView3.as_view(), name='product-list3'),

    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('brand/list/', BrandListAPIView.as_view(), name='category-list'),
    path('brand/create/', BrandCreateAPIView.as_view(), name='category-create'),
    path('brand/update/<int:pk>/', BrandUpdateAPIView.as_view(), name='category-update'),
    path('brand/delete/<int:pk>/', BrandDeleteAPIView.as_view(), name='category-delete'),

    path('color/list/', ColorListAPIView.as_view(), name='category-list'),
    path('color/create/', ColorCreateAPIView.as_view(), name='category-create'),
    path('color/update/<int:pk>/', ColorUpdateAPIView.as_view(), name='category-update'),
    path('color/delete/<int:pk>/', ColorDeleteAPIView.as_view(), name='category-delete'),

    path('mediafiles/list/', MediaFileGetAPIView.as_view(), name='category-list'),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name='category-create'),
    path('mediafiles/delete/<int:pk>/', MediaFileDeleteAPIView.as_view(), name='category-delete'),

    path('product-variants/list/', ProductVariantListAPIView.as_view(), name='category-list'),
    path('product-variants/create/', ProductVariantCreateAPIView.as_view(), name='category-create'),
    path('product-variants/update/<int:pk>/', ProductVariantUpdateAPIView.as_view(), name='category-update'),
    path('product-variants/delete/<int:pk>/', ProductVariantDeleteAPIView.as_view(), name='category-delete'),

    path('size/list/', SizeListAPIView.as_view(), name='category-list'),
    path('size/create/', SizeCreateAPIView.as_view(), name='category-create'),
    path('size/update/<int:pk>/', SizeUpdateAPIView.as_view(), name='category-update'),
    path('size/delete/<int:pk>/', SizeDeleteAPIView.as_view(), name='category-delete'),

    # path('/list/', CRUD.Get.as_view(), name='category-list'),
    # path('/create/', CRUD.Create.as_view(), name='category-create'),
    # path('/update/<int:pk>/', CRUD.Update.as_view(), name='category-update'),
    # path('/delete/<int:pk>/', CRUD.Delete.as_view(), name='category-delete'),
]