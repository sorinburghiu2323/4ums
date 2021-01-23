from django.db import models

# Create your models here.


class Potato(models.Model):
    name = models.CharField(max_length=255)
    is_sweet = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_sweet": self.is_sweet,
            "quantity": self.quantity,
        }
