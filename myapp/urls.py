from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Products API custom",
      default_version='v1',
      description="Description custom",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="usmanalievicjamshid15@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('get-product', index, name='product-index'),
    path('product-update/<int:id>/', patch_product, name='update-product'),
    path('product-create/', create_product, name='create-product'),
    path('product-delete/<int:id>/', product_delete, name='product-delete'),
    path('get-product-by-id/<int:id>/', get_product_by_id, name='get-product-by-id'),
    path('get-category', get_all_category, name='category-all'),
    path('category-update/<int:id>/', patch_category, name='update-category'),
    path('category-create', create_category, name='create-category'),
    path('category-delete/<int:id>/', category_delete, name='category-delete'),
    path('category-get-by-id/<int:id>/', get_category_by_id, name='category-by-id'),
    path('get-customer', get_all_customer, name='customer-all'),
    path('customer-update/<int:id>/', patch_customer, name='update-customer'),
    path('customer-create', create_customer, name='create-customer'),
    path('customer-delete/<int:id>/', delete_customer, name='customer-delete'),
    path('customer-get-by-id/<int:id>/', get_customer_by_id, name='customer-by-id'),
    path('get-busket', get_all_busket, name='busket-all'),
    path('busket-update/<int:id>/', patch_busket, name='update-busket'),
    path('busket-create', create_busket, name='create-busket'),
    path('busket-delete/<int:id>/', category_busket, name='busket-delete'),
    path('busket-get-by-id/<int:id>/', get_busket_by_id, name='busket-by-id'),
    path('get-items', get_all_items, name='item-all'),
    path('item-update/<int:id>/', patch_item, name='update-item'),
    path('item-create', create_item, name='create-item'),
    path('item-delete/<int:id>/', delete_item, name='item-delete'),
    path('item-get-by-id/<int:id>/', get_item_by_id, name='item-by-id'),
    path('summary', summary, name='summary'),
    path('end-date-list', list_of_expired_products, name='list'),
    path('all_sell/<int:pk>/', all_sell, name='all-sell'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('user_id_items/<int:id>/', user_id_items, name='user-id-items'),
    path('kop-sotilgan', kop_sotilgan, name='kop-sotilgan'),
    ]






