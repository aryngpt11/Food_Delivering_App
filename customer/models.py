from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='menu_images/')
    price=models.DecimalField(max_digits=5, decimal_places=2)
    category=models.ManyToManyField('Category', related_name='item')

    def __str__(self):   # The __str__ method in Python classes is used to define a human-readable string representation of an object.
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    items=models.ManyToManyField('MenuItem',related_name='order', blank=True)
    name=models.CharField(max_length=50, blank=True)
    email=models.EmailField(max_length=50 , blank=True)
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

#In Django, the ManyToManyField is a type of field used to establish a many-to-many relationship between two models. It's typically used when each instance of one model can be related to multiple instances of another model, and vice versa.
# %b %d %I: %M %p month name,day ,12 format ,minutes,AM or PM