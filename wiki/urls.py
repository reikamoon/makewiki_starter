from django.urls import path
from wiki.views import PageListView, PageDetailView, PostCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new-page/', PostCreateView.as_view(), name="wiki-new-page"),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
