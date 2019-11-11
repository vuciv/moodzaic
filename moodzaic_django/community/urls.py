from django.urls import path
from . import views

urlpatterns = [
    path('api/community/', views.CommunityListCreate.as_view()),
]