from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator
from django_resized import ResizedImageField


class Category(models.Model):
    catt = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.catt


class Products(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = ResizedImageField(size=[450, 300], upload_to='', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='')
    price = models.IntegerField()
    cat = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_exist = models.BooleanField(default=True)
    quantity = models.IntegerField(blank=False, null=False)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 450 or img.width > 300:
            new_img = (450, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-updated', '-created']

class Order(models.Model):
    total_price = models.FloatField(blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=200, blank=True, null= True)

    def __str__(self):
        self.tracking_code

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.product.title

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

