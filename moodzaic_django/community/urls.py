from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/community/', views.makeCommunity),
    path('api/community/all', views.CommunityListCreate.as_view()),
    url(r'^api/community/(?P<name>[\w]+)$', views.communityDetails),
]