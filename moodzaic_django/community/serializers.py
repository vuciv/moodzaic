from rest_framework import serializers
from community.models import Community
from users.serializers import UserSerializer

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        users = UserSerializer(many=True)
        fields = '__all__'