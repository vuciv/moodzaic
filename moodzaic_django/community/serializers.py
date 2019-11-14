from rest_framework import serializers
from community.models import Community
from users.models import User

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        exclude = ['users']