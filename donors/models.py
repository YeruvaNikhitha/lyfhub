from django.db import models

class Donor(models.Model):

    BLOOD_GROUPS = [
        ('A+','A+'), ('A-','A-'),
        ('B+','B+'), ('B-','B-'),
        ('O+','O+'), ('O-','O-'),
        ('AB+','AB+'), ('AB-','AB-'),
    ]

    AREAS = [
        ('Tirupati','Tirupati'),
        ('Renigunta','Renigunta'),
        ('Chandragiri','Chandragiri'),
        ('Tiruchanoor','Tiruchanoor'),
        ('Alipiri','Alipiri'),
        ('Mangalam','Mangalam'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)

    area = models.CharField(max_length=50, choices=AREAS)

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name