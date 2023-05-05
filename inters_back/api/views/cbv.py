from django.shortcuts import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import District, Product
from api.serializers import DistrictSerializer2, ProductSerializer


class DistrictListAPIView(APIView):
    def get(self, request):
        categories = District.objects.all()
        serializer = DistrictSerializer2(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DistrictSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictDetailAPIView(APIView):
    def get_object(self, district_id):
        try:
            return District.objects.get(pk=district_id)
        except District.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, district_id):
        instance = self.get_object(district_id)
        serializer = DistrictSerializer2(instance)
        return Response(serializer.data)

    def put(self, request, district_id):
        instance = self.get_object(district_id)
        serializer = DistrictSerializer2(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, district_id):
        instance = self.get_object(district_id)
        instance.delete()
        return Response({'deleted': True})

# class ProductListAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class Streets_of_DistrictAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailAPIView(APIView):
#     def get_object(self, product_id):
#         try:
#             return Product.objects.get(pk=product_id)
#         except Product.DoesNotExist as e:
#             return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, product_id):
#         instance = self.get_object(product_id)
#         serializer = ProductSerializer(instance)
#         return Response(serializer.data)

#     def put(self, request, product_id):
#         instance = self.get_object(product_id)
#         serializer = ProductSerializer(instance=instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, product_id):
#         instance = self.get_object(product_id)
#         instance.delete()
#         return Response({'deleted': True})