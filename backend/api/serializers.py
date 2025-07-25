from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Member, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        
        return user
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('_id','MemberId', 'Name', 'role', 'email', 'team', 'createdAt', 'updatedAt')
        read_only_fields = ('createdAt', 'updatedAt')
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('_id', 'title', 'start', 'end', 'allDay', 'createdBy', 'description', 'createdAt', 'updatedAt')
        read_only_fields = ('createdAt', 'updatedAt')
    
