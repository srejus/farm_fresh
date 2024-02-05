from django.db import models

from accounts.models import Account

# Create your models here.
class Feed(models.Model):
    posted_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='posted_by')
    post_content = models.TextField()
    total_likes = models.IntegerField(default=0)
    posted_at = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(null=True,blank=True)

    def is_liked(self, user):
        """
        Check if the given user has liked this post.
        :param user: User instance to check
        :return: True if the user has liked the post, False otherwise
        """
        return self.liked_post.filter(liked_by=user).exists()


class Likes(models.Model):
    post = models.ForeignKey(Feed,on_delete=models.CASCADE,related_name='liked_post')
    liked_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='liked_by')

