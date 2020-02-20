from django.urls import path
from wiki.views import PageListView, PageDetailView
from accounts.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
