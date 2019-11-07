from django.test import TestCase
from users.models import User, Profile

# Create your tests here.
#Hi

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "emil")
    def test_setUsername(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUsername("emil1")
        self.assertEqual("emil1", testUser.getUsername())

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(ProgressScore = 10)
    def test_setUsername(self):
        testProfile = Profile.objects.get(ProgressScore = 10)
        self.assertEqual(10, testProfile.getProgressScore())
        testProfile.setProgressScore(5)
        self.assertEqual(5, testProfile.getProgressScore())
