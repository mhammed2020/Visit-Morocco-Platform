from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Destination(models.Model) :
    name = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='pics', blank=True, null=True)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('post-detail',args=[self.pk] ) #kwargs={'pk': self.pk} used with CBVs


    class Meta :
        ordering = ('-date_posted',)


        



    
