from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView

from products.models import Size
from .serializers import SizeCreateSerializer


class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)