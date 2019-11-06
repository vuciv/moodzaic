from django.db import models
from users.models import User

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

    def setName(self, name):
        self.name = name
        return

    def getName(self):
        return self.name

    def setUsers(self, users):
        self.users = users
        return

    def getUsers(self):
        return self.users.all()

    def addUserToCommunity(self, user):
        self.users.add(user)
        return

    def removeUserFromCommunity(self, user):
        self.users.remove(user)
        return





