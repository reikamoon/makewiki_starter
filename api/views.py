from django.shortcuts import render
from django.contrib.auth.models import User, Group
from wiki.models import Page
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PageSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pages to be viewed or edited.
    """
    queryset = Page.objects.all().order_by('-created')
    serializer_class = PageSerializer
