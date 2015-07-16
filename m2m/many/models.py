from django.db import models


# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=255)
    #parent = models.ForeignKey("self", null=True)
    parents = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.name
