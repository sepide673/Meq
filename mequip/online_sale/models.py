from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Customer(User):
    address = models.TextField(null=True, blank=True)
    national_code = models.CharField(max_length=12, null=True, blank=True)


class Brand(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)


class Category(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    main_category = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.PROTECT)


class Product(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT)
    price = models.FloatField(null=True, blank=True)
    promotion = models.BooleanField(null=True, blank=True, default=False)


class Order(models.Model):
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    value = models.IntegerField(blank=True, null=True)
    discount_value = models.IntegerField(blank=True, null=True)
    final_value = models.IntegerField(blank=True, null=True)


class OrderItem(models.Model):
    created = models.DateField(auto_now_add=True)
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount_price = models.IntegerField(null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True)


