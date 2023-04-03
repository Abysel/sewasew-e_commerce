from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255)

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='frontend/uploads/products')
    slug = models.SlugField(max_length=225)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.get(id_in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products

    def get_all_product_by_adder(adder):
        if adder:
            return Product.objects.filter(add_by=adder)
        else:
            return Product.get_all_products


class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()

    # to save data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def ifExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default=" ", blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer_id(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')


class Featured(models.Model):
    fproduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateStart = models.DateField(default=datetime.datetime.today)
    dateFinsh = models.DateField(default=datetime.datetime.today)
