from django.db import models

# Create your models here.


class UserContactForm(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.TextField(blank=False)

    def __str__(self):
        return self.full_name
