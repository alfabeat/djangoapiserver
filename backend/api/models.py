from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# //   MemberId: string;
# //   Name: string;
# //   role: 'senior' | 'member';
# //     email: string;
# //     team: string;
# //   createdAt?: Date;
# //   updatedAt?: Date;

class Member(models.Model): #This is the model for members
    MEMBER_ROLES = [
        ('senior', 'Senior'),
        ('member', 'Member'),
    ]
    _id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=MEMBER_ROLES)
    email = models.EmailField(max_length=100)
    team = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
#   title: string;
#   start: Date;
#   end: Date;
#   allDay: boolean;
#   createdBy: string; 
#   description?: string;
#   createdAt?: Date;
#   updatedAt?: Date;

class Event(models.Model):#This is the model for events
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    allDay = models.BooleanField(default=False)
    createdBy = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
