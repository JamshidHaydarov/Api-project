from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name





class Category(models.Model):
    name = models.CharField(max_length=100)
    # products = models.ManyToManyField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    expiration_date = models.DateField()
    stock = models.IntegerField()

    # def form_valid(self, form):
    #     form.instance.date_reg = timezone.now()
    #     return super().form_valid(form)


    def __str__(self):
        return self.name

class Busket(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)

    # quantity = models.IntegerField()
    # customer_name = models.CharField(max_length=100)
    # customer_email = models.EmailField()
    # shipping_address = models.TextField()

    def __str__(self):
        return self.owner.name

class Item(models.Model):
    busket = models.ForeignKey(Busket, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name







# Create your models here.
