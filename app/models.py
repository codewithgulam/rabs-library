from turtle import width
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class MyUser(AbstractUser):
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
#     REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS


class Author(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField(max_length=10000 , null=True,blank=True )

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    author=models.ForeignKey( 'Author', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name