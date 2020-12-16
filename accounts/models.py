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
    
    # ----------------------------Tracking User---------------------------

class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',related_name='rel_to_set',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


        



    
