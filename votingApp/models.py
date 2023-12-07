from django.db import models
from django.contrib.auth.models import User
from django.db import migrations, models
from hashlib import sha256
import json
import time
from django.core.exceptions import ValidationError

class number1(models.Model):
    aadhaar=models.CharField(max_length=15,null=True)
    def __str__(self):
        return self.aadhaar

class aadhaarnumber(models.Model):
    useraadhaar=models.CharField(max_length=15,null=True)
    otp=models.CharField(max_length=15,null=True)
    def __str__(self):
        return self.useraadhaar
    
class voteringlist(models.Model):
    image=models.ImageField(upload_to="img/%y")
    leadername=models.CharField(max_length=20,null=True)
    foundation_name=models.CharField(max_length=20,null=True)
    code=models.IntegerField(null=True)
    def __str__(self):
        return self.foundation_name


class votedata(models.Model):
    user = models.IntegerField(null=True, unique=True) 
    leadername = models.IntegerField()
    previous_hash = models.CharField(max_length=64, null=True, blank=True)
    hash = models.CharField(max_length=64, blank=True)
    code = models.IntegerField(null=True) 

    def calculate_hash(self):
        block_data = {
            'leadername': self.leadername,
            'previous_hash': self.previous_hash,
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def save(self, *args, **kwargs):
        self.hash = self.calculate_hash()

        if votedata.objects.filter(user=self.user).exclude(pk=self.pk).exists():
            raise ValidationError("A block with this user already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Block {self.leadername}"
