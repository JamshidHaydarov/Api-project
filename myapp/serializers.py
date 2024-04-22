from rest_framework.serializers import ModelSerializer
from .models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.expiration_date = validated_data.get("expiration_date", instance.expiration_date)


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UpdateCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.address = validated_data.get("address", instance.address)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UpdateCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)


class BucketSerializer(ModelSerializer):
    class Meta:
        model = Busket
        fields = '__all__'


class UpdateBucketSerializer(ModelSerializer):
    class Meta:
        model = Busket
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.owner = validated_data.get("owner", instance.owner)
        instance.date = validated_data.get("date", instance.date)

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class UpdateItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.bucket = validated_data.get("bucket", instance.quantity)
        instance.product = validated_data.get("product", instance.product)
        instance.quantity = validated_data.get("quantity", instance.quantity)
