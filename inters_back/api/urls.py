from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api import views

urlpatterns = [

    path('login/', obtain_jwt_token),

    path('districts/', views.DistrictListAPIView.as_view()),
    path('districts/<int:district_id>/', views.DistrictDetailAPIView.as_view()),

    # path('districts/', views.district_list),
    # path('districts/<int:district_id>/', views.district_detail),
    path('districts/<int:district_id/products/', views.streets_of_district),

    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_detail),
]