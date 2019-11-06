from django.test import TestCase

from community.models import Community
from users.models import User

# Create your tests here.

class CommunityTestCase(TestCase):

    def setUp(self):
        Community.objects.create(name = "fitness")
        User.objects.create(username = "emil")

    def test_setName(self):
        fitnessCommunity = Community.objects.get(name = "fitness")

        fitnessCommunity.setName("fitnessCommunity")
        self.assertEqual("fitnessCommunity", fitnessCommunity.getName())

    def test_addMemberToCommunity(self):
        fitnessUser = User.objects.get(username = "emil")
        fitnessCommunity = Community.objects.get(name = "fitness")

        fitnessCommunity.addUserToCommunity(fitnessUser)
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())

    def test_removeMemberFromCommunity(self):
        fitnessUser = User.objects.get(username = "emil")
        fitnessCommunity = Community.objects.get(name = "fitness")

        fitnessCommunity.addUserToCommunity(fitnessUser)
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())
        fitnessCommunity.removeUserFromCommunity(fitnessUser);
        self.assertNotIn(fitnessUser, fitnessCommunity.getUsers())