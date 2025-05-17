from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView

from products.models import Category
from .serializers import CategoryCreateSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)