# Generated by Django 3.1.4 on 2020-12-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201213_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='about-01.jpg', upload_to='pics'),
        ),
    ]
