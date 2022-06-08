import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager
from utils.models import TimeStampZone
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     

    def create_superuser(self, email, nickname,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

class User(AbstractBaseUser,TimeStampZone, PermissionsMixin):
    objects = UserManager()

    email = models.CharField(max_length=200,unique=True)
    nickname = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    refreshtoken = models.TextField()
    deleted_at = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'nickname',
        'password'
    ]
    
    def __str__(self):
        return self.nickname



    class Meta:
        db_table = 'users'
