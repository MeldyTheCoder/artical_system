from django.db import models
from users.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rims(models.Model):
    firm = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    razboltovka = models.CharField(max_length=120)
    radius = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='rims', null=True, blank=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.firm


class Spares(models.Model):
    title = models.CharField(max_length=100)
    manufactor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='spares')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    rims = models.ForeignKey(to=Rims, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    spares = models.ForeignKey(to=Spares, on_delete=models.CASCADE, null=True, blank=True)


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    rims = models.ForeignKey(to=Rims, on_delete=models.CASCADE, null=True, blank=True)
    spares = models.ForeignKey(to=Spares, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        if self.rims:
            return f"Диски {self.rims.model} - {self.quantity} шт."
        
        return f"Запчасть {self.spares.title} - {self.quantity} шт."

class Order(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    surname = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )
    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    index = models.IntegerField(
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        to=User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    items = models.ManyToManyField(
        to=OrderItem,
        null=False,
        blank=False,
    )