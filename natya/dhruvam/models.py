from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
#class object wise

class Register(AbstractUser):
    SPECIALIZATIONS = [
        ('Choose your specialization', 'Choose your specialization'),
        ('BA Bharathanatyam','BA Bharathanatyam'),
        ('BA Mohiniyattam','BA Mohiniyattam'),
        ('BA Kuchipudi','BA Kuchipudi'),
        ('BA Kathak','BA Kathak'),
        ('BA Odissi','BA Odissi'),
        ('MA Bharathanatyam','MA Bharathanatyam'),
        ('MA Mohiniyattam','MA Mohiniyattam'),
        ('MA Kuchipudi','MA Kuchipudi'),
        ('MA Kathak','MA Kathak'),
        ('MA Odissi','MA Odissi')
    ]
    usertype = models.IntegerField(default=1)
    is_approved = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='guru_images/')
    experience = models.TextField()
    dance_style = models.CharField(max_length=100)
    dance_specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS, default='Choose your specialization',)
    profile_information = models.TextField()

    def _str_(self):
        return self.get_dance_specialization_display()




class Contact(models.Model):
    name=models.CharField(max_length=200,null=True,)
    email=models.CharField(max_length=200,null=True)
    subject=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)



class DanceClass(models.Model):
    DANCE_STYLES = [
        ('bharatanatyam', 'Bharatanatyam'),
        ('mohiniyattam', 'Mohiniyattam'),
        ('kuchipudi', 'Kuchipudi'),
        ('kathak', 'Kathak'),
        ('odissi', 'Odissi'),
    ]

    title = models.CharField(max_length=200)
    video_title = models.TextField(max_length=1000)
    video_link = models.URLField()
    dance_style = models.CharField(max_length=50, choices=DANCE_STYLES)
    description = models.TextField()
    image = models.ImageField(upload_to='dance_class_images/', default='')
    guru = models.ForeignKey(Register, on_delete=models.CASCADE, default='')