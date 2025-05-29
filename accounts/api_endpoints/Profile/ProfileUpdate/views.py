from rest_framework import permissions, parsers
from rest_framework.generics import UpdateAPIView, GenericAPIView

from accounts.models import User
from .serializer import ProfileUpdateSerializer


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_object(self):
        return User.objects.filter(id=self.request.user.id).first()
