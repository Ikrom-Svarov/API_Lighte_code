# from django.test import TestCase

# # Create your tests here.
# from rest_framework import generics, filters
# from .models import User, Product
# from .serializers import UserSerializer, ProductSerializer

# class UserProductListView(generics.ListAPIView):
#     queryset_user = User.objects.all()
#     queryset_product = Product.objects.all()
#     serializer_user = UserSerializer
#     serializer_product = ProductSerializer
#     filter_backends = [filters.OrderingFilter, filters.SearchFilter]
#     ordering_fields = ['user_field', 'product_field']  # Замените на реальные поля моделей
#     search_fields = ['user_field', 'product_field']  # Замените на реальные поля моделей

#     def get_queryset(self):
#         # Вы можете применить дополнительные фильтры, если необходимо
#         queryset_user = self.queryset_user
#         queryset_product = self.queryset_product

#         # Применение фильтров к каждой базе данных
#         # Замените на соответствующие поля и значения фильтрации
#         user_filter = self.request.query_params.get('user_filter', None)
#         if user_filter:
#             queryset_user = queryset_user.filter(user_field=user_filter)

#         product_filter = self.request.query_params.get('product_filter', None)
#         if product_filter:
#             queryset_product = queryset_product.filter(product_field=product_filter)

#         return queryset_user, queryset_product

#     def list(self, request, *args, **kwargs):
#         queryset_user, queryset_product = self.get_queryset()
#         serializer_user = self.serializer_user(queryset_user, many=True)
#         serializer_product = self.serializer_product(queryset_product, many=True)
#         combined_data = {
#             'users': serializer_user.data,
#             'products': serializer_product.data,
#         }
#         return Response(combined_data)
