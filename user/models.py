from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class User(models.Model):
    gender_choices = ( 
        ('F','Female'),
        ('M', 'Male')
    )
    first_name=models.CharField(max_length=80, blank=False, null=False, verbose_name='first name')
    last_name=models.CharField(max_length=80, blank=False, null=False, verbose_name='last name')
    address=models.TextField(blank=True, null=True, verbose_name='address')
    phone_number=models.CharField(max_length=20, blank=True, null=True, verbose_name='phone number')
    gender=models.CharField(max_length=1, blank=False, null=False, verbose_name='gender', choices=gender_choices)
    create_at=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tbl_user'

class CustomUserAuth(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table='tbl_custom_user_auth'

    def __str__(self):
        return self.username