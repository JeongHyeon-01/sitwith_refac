import re
from .models import User
from django.forms import ValidationError

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$'

def validate_password(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError("Invalid password")
    
def validate_email(email):
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError("Invalid email")

class SignupSirializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
    ),
    password = serializers.CharField(
        required=True,
        write_only = True,
    )
    password2 = serializers.CharField(write_only = True, required=True)
    
    class Meta:
        model = User
        fields = ('email','password','password2','username')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        validate_email(data['email'])
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        token = RefreshToken.for_user(user)
        user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.save()
    
        return user

class SigninSirializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required = True,
        write_only = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
        style= {'input_type' : 'password'}
    )
    class Meta(object):
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        email = data.get('email',None)
        password = data.get('password',None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError('Check Your Email or Password')
        
        else:
            raise serializers.ValidationError("User does not exist")
        

        token = RefreshToken.for_user(user=user)
        data = {
            'user' : user.id,
            'refresh_token' : str(token),
            'access_token' : str(token.access_token)
        }
        user.refreshtoken = token
        user.save()
        return data




 