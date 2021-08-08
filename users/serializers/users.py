""" Users Serializers """

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """ Profile model serializer """

    class Meta:
        model = Profile
        fields=['address','postalCode','city','country','phoneNumber','cc_number','cc_expiry','cc_code']


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """

    profile = ProfileSerializer()

    class Meta:
    
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile']
    
    def update(self, instance, validated_data):
    
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.address = profile_data.get('address', profile.address)
        profile.postalCode = profile_data.get('postalCode', profile.postalCode)
        profile.city = profile_data.get('city', profile.city)
        profile.country = profile_data.get('country', profile.country)
        profile.phoneNumber = profile_data.get('phoneNumber', profile.phoneNumber)
        
        profile.cc_number = profile_data.get('cc_number', profile.cc_number)
        profile.cc_expiry = profile_data.get('cc_expiry', profile.cc_expiry)
        profile.cc_code = profile_data.get('cc_code', profile.cc_code)

        profile.save()

        return instance    
        
class NewUserSerializer(serializers.ModelSerializer):
    ''' Return the data for a new user '''

    class Meta:
        model = User
        fields=['username']