from django.urls import path
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('api/community/', views.CommunityListCreate.as_view()),
    path('api/community/', views.comDet),
    url(r'^api/community/(?P<name>[\w]+)$', csrf_exempt(views.communityDetails))
]
