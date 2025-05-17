from rest_framework import serializers

from products.models import Brand


class BrandGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
