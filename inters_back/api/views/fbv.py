from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from api.models import Product, District
from api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer =ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer =ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted': True})
def streets_of_district(request, district_id):
    # products = Product.objects.all()
    # products_json = [p.to_json() for p in products]

    # district = District.objects.get(pk= district_id)
    

    # for product in products_json:
    #     if product['district'] == district.id:
    #         matching_products.append(product)

    # if len(matching_products) != 0:
    #     return JsonResponse(matching_products,safe=False,json_dumps_params={'indent':2})
    # return JsonResponse({'error':'products not found'})
    try:
        matching_products = []
        products_json = [p.to_json() for p in Product.objects.all()]
        for i in products_json:
            if i['district']==District.objects.get(pk = District.objects.get(pk= district_id)):
                matching_products.append(i)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = ProductSerializer(matching_products, many = True)
        return Response(serializer.data)
    