
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class Badge(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class Badge(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')
