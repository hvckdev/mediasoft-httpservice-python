from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField()
    opens_at = models.TimeField()
    closes_at = models.TimeField()

    def __str__(self):
        return self.name
