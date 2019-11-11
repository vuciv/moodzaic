from django.db import models
from users.models import User

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

    def setName(self, name):
        if (name != '') and name.isalnum() and (len(name) <= 30):
            self.name = name
        return

    def getName(self):
        return self.name

    # can you use a setter for a ManyToMany relationship in django...?
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

class Post(models.Model):
    post = models.CharField(max_length=1000)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def setPost(self, post):
        if (len(post) > 0 and len(post) <= 1000):
            self.post = post
        return

    def getPost(self):
        return self.post

    def setCommunity(self, community):
        self.community = community
        return

    def getCommunity(self):
        return self.community

    def setPoster(self, poster):
        self.poster = poster
        return

    def getPoster(self):
        return self.poster

    #TODO TIME?

## Ahh! A data-class!
## IDK what to do about this because you can't have recursive objects.
class Comment(Post):
    originalPost = models.ForeignKey(Post, related_name='+', on_delete=models.CASCADE)

    def setOriginalPost(self, originalPost):
        self.originalPost = originalPost
        return

    def getOriginalPost(self):
        return self.originalPost
