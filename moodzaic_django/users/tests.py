from django.test import TestCase
from users.models import User, Profile, Goal


# Create your tests here.
#Hi

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
    def test_setUsernameNotStringFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserUsername(13))

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
    def test_setUserAgeNotIntFailure(self):
        testUser = User.objects.get(username = "emil")
        self.assertFalse(testUser.setUserAge("emil"))

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
    
    def test_setGoalGoalSuccess(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        testGoal.setGoalGoal("Drink more water")
        self.assertEqual("Drink more water", testGoal.goal)
    def test_setGoalGoalLengthFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalGoal("1234567890123456789012345678901"))
    def test_setGoalGoalNotStringFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalGoal(1))

    def test_setGoalFrequencySuccess(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        testGoal.setGoalFrequency(3)
        self.assertEqual(3, testGoal.frequency)
    def test_setGoalFrequencyNotIntFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalFrequency("emil"))

    def test_setGoalTimeSuccess(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        testGoal.setGoalTime("14:00")
        self.assertEqual("14:00", testGoal.time)
    def test_setGoalTimeAMPMFormatFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalTime("2:00 PM"))
    def test_setGoalTimeNoPaddingFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalTime("1:00"))
    def test_setGoalTimeNotStringFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalTime(2))
    def test_setGoalTimeBadHourFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalTime("25:19"))
    def test_setGoalTimeBadMinuteFailure(self):
        testGoal = Goal.objects.get(goal = "Drink water")
        self.assertFalse(testGoal.setGoalTime("13:62"))

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(ProgressScore = 10)
    def test_setUsername(self):
        testProfile = Profile.objects.get(ProgressScore = 10)
        self.assertEqual(10, testProfile.getProgressScore())
        testProfile.setProgressScore(5)
        self.assertEqual(5, testProfile.getProgressScore())