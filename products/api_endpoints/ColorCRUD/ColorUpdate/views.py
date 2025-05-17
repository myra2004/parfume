from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, GenericAPIView

from products.models import Color
from .serializers import ColorUpdateSerializer


class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)