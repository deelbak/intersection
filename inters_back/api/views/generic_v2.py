from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import District, Product
from api.serializers import DistrictSerializer2, ProductSerializer


class DistrictListAPIView(generics.ListCreateAPIView):
    serializer_class = DistrictSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ProductListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DistrictDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictSerializer2
    lookup_url_kwarg = 'district_id'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

