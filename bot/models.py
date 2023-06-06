from django.db import models

# Create your models here.

class BotUsers(models.Model):
    fullname = models.CharField(max_length=100)
    user_id  = models.CharField(max_length=100)
    user_step = models.CharField(max_length=100, blank=True)
    user_lang = models.CharField(max_length=10, blank=True)
    user_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.fullname