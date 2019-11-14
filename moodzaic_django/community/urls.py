from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/community/', views.makeCommunity),
    # url(r'^api/community/(?P<name>[\w]+)$', views.communityDetails),
]