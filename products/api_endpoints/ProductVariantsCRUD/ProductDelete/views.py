from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, DestroyAPIView

from products.models import ProductVariant


class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)