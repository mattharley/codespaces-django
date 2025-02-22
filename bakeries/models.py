from django.db import models

class Bakery(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    cuisine = models.CharField(max_length=255)
    rating = models.IntegerField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
