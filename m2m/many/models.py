from django.db import models


# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=255)
    #parent = models.ForeignKey("self", null=True)
    elements_connected = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name
