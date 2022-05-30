import datetime
from django.db import models
from utils.models import TimeStampZone
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser,TimeStampZone):
    email = models.CharField(max_length=200,unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    refreshtoken = models.CharField(max_length=200)
    deleted_at = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'
