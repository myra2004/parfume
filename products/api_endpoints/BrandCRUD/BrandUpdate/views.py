from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, GenericAPIView

from products.models import Brand
from .serializers import BrandUpdateSerializer


class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)