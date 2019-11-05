from django.test import TestCase
from users.models import User, Goal

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "emil", password = "snibby")

    def test_setUsernameSuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserUsername("emil1")
        self.assertEqual("emil1", testUser.username)
    def test_setUsernameLengthFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserUsername("123456789012345678901"))

    def test_setUserPasswordSuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserPassword("snibby2")
        self.assertEqual("snibby2", testUser.password)
    def test_setUserPasswordTooLongFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserPassword("123456789012345678901"))
    def test_setUserPasswordTooShortFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserPassword("1234567"))

    def test_setUserAgeSuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserAge(21)
        self.assertEqual(21, testUser.age)
    def test_setUserAgeTooYoungFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserAge(17))

    def test_setUserGenderManSuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserGender('man')
        self.assertEqual('man', testUser.gender)
    def test_setUserGenderWomanSuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserGender('woman')
        self.assertEqual('woman', testUser.gender)
    def test_setUserGenderNonbinarySuccess(self):
        testUser = User.objects.get(username = "emil")
        testUser.setUserGender('nonbinary')
        self.assertEqual('nonbinary', testUser.gender)
    def test_setUserGenderFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserGender('gibberish'))


class GoalTestCase(TestCase):
    def setUp(self):
        Goal.objects.create(goal = "Drink water", frequency = "5", time = "16:00 AM")
    
    def test_setGoalGoal(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        testGoal.setGoalGoal("Drink more water")
        self.assertEqual("Drink more water", testGoal.goal)