from rest_framework.generics import DestroyAPIView, GenericAPIView
from rest_framework import permissions

from accounts.models import User


class ProfileDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()