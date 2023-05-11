from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Vehicle(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    NUMBER_CHOICES = (
        ('1', 'Two wheeler'),
        ('2', 'Three wheeler'),
        ('3', 'Four wheeler'),

    )

    number=models.CharField(max_length=250, validators=[alphanumeric])
    type =models.CharField(max_length=250, choices=NUMBER_CHOICES)
    model=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(upload_to='pics',default='gallery')




    def __str__(self):
        return self.number
