from community.models import Community
from community.serializers import CommunitySerializer
from rest_framework import generics

class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer