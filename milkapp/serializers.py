from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

User._meta.get_field('email')._unique = True

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','image','phone','address','is_store','is_customer','is_deliveryBoy','latitude',\
            'longitude','push_token')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','image','phone','address','is_store','is_customer','is_deliveryBoy')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
         model=User
         fields=('username','password') 
    

class DeliveryBoySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBoy
        fields = ['user']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['user']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = "__all__"

# class CitySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     pincode = serializers.CharField(max_length=50)
#     lat = serializers.CharField(max_length=50)
#     lng = serializers.CharField(max_length=50)
#     owner_id = serializers.IntegerField()

#     def create(self,validated_data):
#         return City.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.pincode = validated_data.get('pincode', instance.pincode)
#         instance.lat = validated_data.get('lat', instance.lat)
#         instance.lng = validated_data.get('lng', instance.lng)
#         instance.save()
#         return instance

