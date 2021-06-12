from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

CATEGORY_CHOICES =(
    ('SB','GIÀY NAM'),
    ('SG','GIÀY NỮ'),
    ('SK','GIÀY TRẺ EM')
)

CHOOSE_SIZE = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

CHOOSE_COLOR=(
    ('Purple','Purple'),
    ('Red', 'Red'),
    ('Blue', 'Blue')
)

PAYMENT_CHOICE = (
    ('Cash', 'Cash'),
    ('Transfermoney', 'Transfermoney'),
    ('Shipcode', 'Shipcode')
)

class Product(models.Model):
    Name= models.CharField(max_length=255)
    price=models.FloatField(max_length=255)
    description = models.TextField()
    date =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=255)
    discount = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
def __str__(self):
    return self.Name


class Address(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    def __str__(self):
        return self.address
        
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='ProductOrder')
    number=models.IntegerField(default=1)
    producsize=models.CharField(max_length=255,choices=CHOOSE_SIZE)
    choosesizecolor=models.ForeignKey('ChooseSizeColor', on_delete=models.CASCADE, related_name='choosesizecolor')
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product.Name

    def TotalOderProduct(self):
        return self.number * self.product.price
        
class Myorder(models.Model):
    infomationUsers=models.ForeignKey('InfomationUsers', on_delete=models.SET_NULL,blank=True,null=True)
    payment=models.ForeignKey('Payment', on_delete=models.SET_NULL,blank=True,null=True)
    Address=models.ForeignKey('Address',on_delete=models.CASCADE,blank=True,null=True, related_name='Address')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Order,related_name='ProductMyorder')
    Payment=models.ForeignKey('Payment', on_delete=models.SET_NULL,blank=True,null=True, related_name='Payment1')
    date =models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
  

class Payment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    adress=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    bridday=models.CharField(max_length=255)
    identify=models.CharField(max_length=255)
    paymentoption=models.CharField(max_length=255,choices=PAYMENT_CHOICE)
    address=models.ForeignKey('Address', on_delete=models.SET_NULL,blank=True,null=True, related_name='Addresspayment')
    def __str__(self):
        return '%s || %s' % (self.paymentoption, self.adress)

class InfomationUsers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    adress=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    bridday=models.CharField(max_length=255)
    identify=models.CharField(max_length=255)
    address=models.ForeignKey('Address', on_delete=models.SET_NULL,blank=True,null=True, related_name='AddressUser')
    def __str__(self):
        return self.user.username

class ChooseSizeColor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producsize=models.CharField(max_length=255,choices=CHOOSE_SIZE)
    producColor=models.CharField(max_length=255,choices=CHOOSE_COLOR)
    status = models.BooleanField(default=False)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return '%s and %s' % (self.producsize, self.producColor)

class Comment (models.Model):
    ProductComemnt = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Stars = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="images/",blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)