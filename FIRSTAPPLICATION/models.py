from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=30)

class ID(models.Model):
    ID=models.CharField(max_length=30)


class Contact(models.Model):
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=30)