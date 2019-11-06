from django.test import TestCase

from community.models import Community
from users.models import User

# Create your tests here.

class CommunityTestCase(TestCase):

    def setUp(self):
        Community.objects.create(name = "fitness")

    def test_setName(self):
        fitnessCommunity = Community.objects.get(name = "fitness")
        fitnessCommunity.setName("fitnessCommunity")
        self.assertEqual("fitnessCommunity", fitnessCommunity.getName())