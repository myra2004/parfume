from rest_framework import serializers

from products.models import Category


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'