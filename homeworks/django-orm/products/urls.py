from django.urls import path
from .views import add_product, product_details, show_products

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/show_products", show_products, name="show_products")
]