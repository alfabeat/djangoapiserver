from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, MemberSerializer, EventSerializer, MemberEditSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Member, Event
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """
    View to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Allow any user to create an account

class MemberListView(generics.ListCreateAPIView):
    """
    View to list and create members.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_queryset(self):
  
        return Member.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else: 
            print(serializer.errors)
            # No additional code needed here for edit functionality.
class MemberDetailView(generics.ListCreateAPIView):
    """
    View to retrieve or update a member by ID.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id is not None:
            return Member.objects.filter(_id=id)
        return Member.objects.none()
class MemberEditView(generics.UpdateAPIView):
    """
    View to edit a member.
    """
    queryset = Member.objects.all()
    serializer_class = MemberEditSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_object(self):
        id = self.request.query_params.get('id')
        if id is not None:
            try:
                return Member.objects.get(_id=id)
            except Member.DoesNotExist:
                raise NotFound('Member not found.')
        raise ParseError('Missing id query parameter.')
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

class MemberDeleteView(generics.DestroyAPIView):
    """
    View to delete a member.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_object(self):
        id = self.request.query_params.get('id')
        if id is not None:
            try:
                member = Member.objects.get(_id=id)

                return member
            except Member.DoesNotExist:
                raise NotFound('Member not found.')

        raise ParseError('Missing id query parameter.')
    def delete(self, request, *args, **kwargs):
        member = self.get_object()
        member.delete()
        return Response({'message': 'Member deleted successfully.'}, status=200)

class EventListView(generics.ListCreateAPIView):
    """
    View to list and create Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_queryset(self):
  
        return Event.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else: 
            print(serializer.errors)
            # No additional code needed here for edit functionality.
class EventDetailView(generics.ListCreateAPIView):
    """
    View to retrieve or update a Event by ID.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id is not None:
            return Event.objects.filter(_id=id)
        return Event.objects.none()


class EventDeleteView(generics.DestroyAPIView):
    """
    View to delete a Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_object(self):
        id = self.request.query_params.get('id')
        if id is not None:
            try:
                return Event.objects.get(_id=id)
            except Event.DoesNotExist:
                raise NotFound('Event not found.')
        raise ParseError('Missing id query parameter.')
    def delete(self, request, *args, **kwargs):
        event = self.get_object()
        event.delete()
        return Response({'message': 'event deleted successfully.'}, status=200)
class EventEditView(generics.UpdateAPIView):
    """
    View to edit a Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_object(self):
        id = self.request.query_params.get('id')
        if id is not None:
            try:
                return Event.objects.get(_id=id)
            except Event.DoesNotExist:
                raise NotFound('Event not found.')
        raise ParseError('Missing id query parameter.')
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
