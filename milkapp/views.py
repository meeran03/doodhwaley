from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets,serializers
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        login(request, user)
        print(request)
        return super(LoginView, self).post(request, format=None)

    def get_post_response_data(self, request, token, instance):
        UserSerializer2 = UserSerializer

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token,

        }
        if UserSerializer is not None:
            data["user"] = UserSerializer2(
                request.user,
                context=self.get_context()
            ).data
        return data

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeliveryBoyViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryBoySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DeliveryBoy.objects.all()

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Store.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Order.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Order.objects.all()
        customer = self.request.query_params.get('customer', None)
        status = self.request.query_params.get('status', None)
        if customer is not None:
            queryset = queryset.filter(customer=customer)
            if status is not None:
                queryset = queryset.filter(status=status)
        return queryset

class OrderProductViewSet(viewsets.ModelViewSet):
    serializer_class = OrderProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = OrderProduct.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProductCategory.objects.all()

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscription.objects.all()

class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SubscriptionType.objects.all()

class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Banner.objects.all()

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notification.objects.all()

class ComplainViewSet(viewsets.ModelViewSet):
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Complain.objects.all()


# class CityAPI(generics.ListCreateAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


# class city_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#     permission_classes = [permissions.IsAuthenticated]
