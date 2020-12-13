from django.db import models

# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email