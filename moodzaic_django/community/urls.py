from django.urls import path
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
<<<<<<< HEAD
    # path('api/community/', views.CommunityListCreate.as_view()),
    path('api/community/', views.comDet),
    url(r'^api/community/(?P<name>[\w]+)$', csrf_exempt(views.communityDetails))
]
=======
    path('api/community/', views.makeCommunity),
    url(r'^api/community/(?P<name>[\w]+)$', views.communityDetails),
]
>>>>>>> 76b65dfb6043e2b7e2258cb24249f0c89f024fd5
