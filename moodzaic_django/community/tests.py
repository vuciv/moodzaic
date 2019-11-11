from django.test import TestCase

from community.models import Community, Post
from users.models import User

# Create your tests here.

# Testing our communities implementation and behaviour
class CommunityTestCase(TestCase):

    def setUp(self):
        Community.objects.create(name = "fitness")
        Community.objects.create(name = "sleep")
        User.objects.create(username = "emil")
        User.objects.create(username = "jersey")

    def test_getName(self):
        fitnessCommunity = Community.objects.get(name = "fitness")
        self.assertEqual("fitness", fitnessCommunity.getName())

    def test_setName(self):
        fitnessCommunity = Community.objects.get(name = "fitness")
        self.assertEqual("fitness", fitnessCommunity.getName())

        fitnessCommunity.setName("fitnessCommunity")
        self.assertEqual("fitnessCommunity", fitnessCommunity.getName())

        fitnessCommunity.setName("")
        self.assertEqual("fitnessCommunity", fitnessCommunity.getName())

        fitnessCommunity.setName("r")
        self.assertEqual("r", fitnessCommunity.getName())

        fitnessCommunity.setName("cwyZva1ZPOBu2UchlBAU0rXpQOr7X") #29 chars
        self.assertEqual("cwyZva1ZPOBu2UchlBAU0rXpQOr7X", fitnessCommunity.getName())

        fitnessCommunity.setName("cwyZva1ZPOBu2UchlBAU0rXpQOr7X0") #30 chars
        self.assertEqual("cwyZva1ZPOBu2UchlBAU0rXpQOr7X0", fitnessCommunity.getName())

        fitnessCommunity.setName("cwyZva1ZPOBu2UchlBAU0rXpQOr7X00") #31 chars
        self.assertEqual("cwyZva1ZPOBu2UchlBAU0rXpQOr7X0", fitnessCommunity.getName())

        fitnessCommunity.setName("hello world")
        self.assertEqual("cwyZva1ZPOBu2UchlBAU0rXpQOr7X0", fitnessCommunity.getName())

        fitnessCommunity.setName("  ")
        self.assertEqual("cwyZva1ZPOBu2UchlBAU0rXpQOr7X0", fitnessCommunity.getName())

        fitnessCommunity.setName("123")
        self.assertEqual("123", fitnessCommunity.getName())

        fitnessCommunity.setName("abc123%")
        self.assertEqual("123", fitnessCommunity.getName())

        fitnessCommunity.setName("NULL")
        self.assertEqual("NULL", fitnessCommunity.getName())

    def test_getUsers(self):
        fitnessCommunity = Community.objects.get(name = "fitness")
        fitnessUser = User.objects.get(username = "emil")
        fitnessUser2 = User.objects.get(username = "jersey")

        self.assertEqual(0, fitnessCommunity.getUsers().count())

        fitnessCommunity.users.add(fitnessUser)
        qs = fitnessCommunity.getUsers()
        self.assertEqual(1, qs.count())
        self.assertEqual(fitnessUser, qs[0])

        fitnessCommunity.users.add(fitnessUser2)
        self.assertEqual(2, fitnessCommunity.getUsers().count())

    def test_addUserToCommunity(self):
        fitnessUser = User.objects.get(username = "emil")
        fitnessCommunity = Community.objects.get(name = "fitness")

        fitnessCommunity.addUserToCommunity(fitnessUser)
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())

        fitnessCommunity.addUserToCommunity(fitnessUser)
        self.assertEqual(1, fitnessCommunity.getUsers().count())
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())

    def test_removeUserFromCommunity(self):
        fitnessUser = User.objects.get(username = "emil")
        fitnessUser2 = User.objects.get(username = "jersey")
        fitnessCommunity = Community.objects.get(name = "fitness")

        fitnessCommunity.addUserToCommunity(fitnessUser)
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())
        fitnessCommunity.removeUserFromCommunity(fitnessUser2);
        self.assertIn(fitnessUser, fitnessCommunity.getUsers())
        fitnessCommunity.removeUserFromCommunity(fitnessUser);
        self.assertNotIn(fitnessUser, fitnessCommunity.getUsers())

class PostTestCase(TestCase):

    def setUp(self):
        Community.objects.create(name = "fitness")
        Community.objects.create(name = "sleep")
        User.objects.create(username = "emil")
        User.objects.create(username = "jersey")
        fitnessCommunity = Community.objects.get(name = "fitness")
        fitnessUser = User.objects.get(username = "emil")
        Post.objects.create(post = "Hello world", community = fitnessCommunity, poster = fitnessUser)

        # also tests getPost
    def test_setPost(self):
        firstPost = Post.objects.get(post = "Hello world")

        firstPost.setPost("Hi!")
        self.assertEqual("Hi!", firstPost.getPost())

        firstPost.setPost("")
        self.assertEqual("Hi!", firstPost.getPost())

        firstPost.setPost("#%()")
        self.assertEqual("#%()", firstPost.getPost())

        firstPost.setPost("   ")
        self.assertEqual("   ", firstPost.getPost())

        firstPost.setPost("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms") #999 chars
        self.assertEqual("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms", firstPost.getPost())

        firstPost.setPost("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms1") #1000 chars
        self.assertEqual("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms1", firstPost.getPost())

        firstPost.setPost("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms11") #1001 chars
        self.assertEqual("6yWcC4W8mj5EGL686wYKTtDkIGrX0CAgS92ll9R47MgkKbSI66rWnk7y490hXP7wK8Y1bmdkAJrmtYVJ52IcMynYYz5YBwFSptiugcUclJlCxUkeGiS1ZnKP3o7jKwtkCf33rhwv8V3wJYQVLTg8KpOgjmQQHpRfGlv2zJGcukayda2CN9jQzo2nlQpfWzNVgvsNmgBZzskAYjmd2gxASfBHCGeOXzR2ui652z7HIRIrYrm2LEOwm9evex7sN1TazauvRTKKCa2av5AGeQsXCIqy1QXtQbClxkvFNY1yqPe205QkrdGwS8YavAqfMdIjje7mSlxklntVkQAJeKL9XuctwhFidQewwdpZ1q0PEBpUcF2U7xzJOYqIcMJoUqf2FFc5qOYK9DtVaqj1JurCFA4YLFn1gudz3yT0NZ1ONGa5qhPSDQ33fKNZhczlkEnAgtaCPHDLaYZ7c7I6Hp3RX3OyCJRWudmywYvQqSZtC1ZHH7j6jYcGyG0ApGJiKuRPVjGUhqSlqeuRAiOSUOQ4qtJrVFN3wBVT0nXv72Ddr1KsUTNTa5c2946lcKxQat9mjBwt2FrHNkXSPHymzOWBm8eMoX6DlmBLK3N0XILiSO3eUTBeKDE0Iuxh7Q27msI7iLGtDTnLddbPGcIRcETTnApLMDtCVrXxZQxoHuuVw6j3cAtj8NI73r4uxy6VGK3LevvLgJQM8nqcoF7Hn0lGoZHjQjTgeHJxLwDl4esfS4GnYRFRIQlIYUPKYznKD4SGPnlSzME7H4TCuhVqabjn5SBwW3N9CqGF4O1iaVzfhs77rVi4DbAVqvuKSscwUpIR60U5b3HoPEx4SOdhw8YBswAwHaqoh5aE0uaihlEF5xJAQM4mgqs8myDtCMd1WGbYiZMjd7zUgyUIXWnLMXch7yP6c0DcdhPn5hxt0FtcGp0sU7hxNgIN4ePVWsGIi9b74kVXhcDOCO83YmqG3eMtUm9jKmKDWQyhYhswCms1", firstPost.getPost())

    # also tests getCommunity
    def test_setCommunity(self):
        firstPost = Post.objects.get(post = "Hello world")
        newCommunity = Community.objects.get(name = "sleep")

        self.assertEqual("fitness", firstPost.getCommunity().getName())

        firstPost.setCommunity(newCommunity)
        self.assertEqual(newCommunity, firstPost.getCommunity())

    # also tests getPoster
    def test_setPoster(self):
        firstPost = Post.objects.get(post = "Hello world")
        fitnessUser = User.objects.get(username = "emil")
        fitnessUser2 = User.objects.get(username = "jersey")

        self.assertEqual(fitnessUser, firstPost.getPoster())

        firstPost.setPoster(fitnessUser2)
        self.assertEqual(fitnessUser2, firstPost.getPoster())
