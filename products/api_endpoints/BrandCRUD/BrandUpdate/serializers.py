from rest_framework import serializers

from products.models import Brand


class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'id'
