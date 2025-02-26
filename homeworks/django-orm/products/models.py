from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    approved_by = models.ForeignKey(User, related_name="approved_by", null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    display_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title
