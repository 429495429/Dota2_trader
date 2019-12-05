import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Decorations(models.Model):
	decoration_name = models.CharField(max_length=200)
    decoration_champion = models.CharField(max_length=50)
    decoration_part = models.CharField(max_length=50)
    decoration_rarelity = models.CharField(max_length=50)
    decoration_average_price = models.Double(max=9999.99)

    def __str__(self):
    	return self.decoration_name

    def recent_average_price(self):
    	return self.decoration_average_price

class Items(models.Model):
    item_id = models.Integer(max_digit=10)
	item_type = models.ForeignKey(Decorations, on_delete=models.CASCADE)
    publisher_id = models.CharField(max_length=50)
    price = models.Double(max=9999.99)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f" {self.item_type} ${price} by {publisher_id}"