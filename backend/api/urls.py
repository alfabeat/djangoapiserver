from django.urls import path
from . import views
urlpatterns = [#this the url paths for the api
    path('user/regi/', views.CreateUserView.as_view(), name='create_user'),
    path('members/', views.MemberListView.as_view(), name='member_list'),
    path('members/getid/', views.MemberDetailView.as_view(), name='member_detail'),
    path('members/delete', views.MemberDeleteView.as_view(), name='member_delete'),
    path('members/edit', views.MemberEditView.as_view(), name='member_edit'),
    path('events/', views.EventListView.as_view(), name='Event_list'),
    path('events/getid/', views.EventDetailView.as_view(), name='Event_detail'),
    path('events/delete', views.EventDeleteView.as_view(), name='Event_delete'),
    path('events/edit', views.EventEditView.as_view(), name='Event_edit'),
    
]
