from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
   
    title = models.TextField(max_length=200)
    slug = models.SlugField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    #group_id = models.ForeignKey(Group)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group, blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='group'
    )
