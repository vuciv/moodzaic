from django.test import TestCase
from users.models import User

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "emil")
    def test_setUsername(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUsername("emil1")
        self.assertEqual("emil1", testUser.getUsername())