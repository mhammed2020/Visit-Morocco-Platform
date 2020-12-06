from django.db import models

class Destination(models.Model) :
    name = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    
