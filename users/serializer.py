import re, jwt
from .models import User
from django.forms import ValidationError
from django.conf import settings
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
        fields = ('email','password','password2','nickname')
    
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
            nickname = validated_data['nickname'],
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
        

        refresh_token = RefreshToken.for_user(user=user)
        access_token = refresh_token.access_token

        decode_jwt = jwt.decode(str(access_token), settings.SECRET_KEY, algorithms="HS256")

        decode_jwt['is_staff'] = user.is_staff
        decode_jwt['is_admin'] = user.is_admin
        
        encode_jwt = jwt.encode(decode_jwt, settings.SECRET_KEY, algorithm="HS256").decode('utf-8')
        data = {
            'user' : user.id,
            'refresh_token' : str(refresh_token),
            'access_token' : str(encode_jwt)
        }
        user.refreshtoken = refresh_token
        user.save()
        return data




 