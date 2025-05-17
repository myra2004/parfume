from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, GenericAPIView

from products.models import Category
from .serializers import CategoryUpdateSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)