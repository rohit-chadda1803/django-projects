from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from .models import Note

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only = True,
        required= True ,
        validators = [validate_password],
        style = {'input_type':'password'}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )  # confirm pass . 

    class Meta: 
        model = User 
        fields = ('username', 'email', 'password', 'password2')

    def validate(self , attrs):#both pass must same---- OBJECT LEVEL VALIDATION.  
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs 

    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists. "
            )
        return value

    def create(self, validated_data):
        # Remove password2 since it's not a field on the User model
        validated_data.pop("password2")

        # create_user() automatically hashes the password before storing it.

        user = User.objects.create_user(**validated_data)


        #drf expects created obj to be retured . 
        return user


       



# class NoteSerializer(serializers.ModelSerializer):
#     class Meta : 
#         model = Note 
#         fields = '__all__'
#         read_only_fields =['user','created_at','updated_at'] #can be sent in api response but can't be modified by incoming api data