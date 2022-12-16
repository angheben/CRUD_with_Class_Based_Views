from django.urls import path

from .views import IndexView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/", CreateProductView.as_view(), name='add_product'),
    path('<int:pk>/update/', UpdateProductView.as_view(), name='update_product'),
    path('<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
]
