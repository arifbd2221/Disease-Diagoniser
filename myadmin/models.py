from django.db import models

class User(models.Model):
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })

    email = models.CharField(max_length=100, blank=True, null=True)
    gender_list = (('male', 'Male'), ('female', 'Female'),)
    gender = models.CharField(max_length=10, choices=gender_list, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    chamber = models.CharField(max_length=100, blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return self.email