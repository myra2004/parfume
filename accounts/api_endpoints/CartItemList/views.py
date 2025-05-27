from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import *
from accounts.models import CartItem


class CartItemListAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer_data = serializer_class(self.get_queryset(), many=True)
        serializer_data.is_valid(raise_exception=True)

        return Response(serializer_data.data, status=status.HTTP_200_OK)