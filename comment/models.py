from django.db import models
from user.models import User
from post.models import Post


# Create your models here.
class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tbl_comment_post'

class LikePost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like = models.BooleanField()
    
    class Meta:
        db_table='tbl_like_post'

class LikeComment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.OneToOneField(CommentPost, on_delete=models.CASCADE)
    like = models.BooleanField()

    class Meta:
        db_table='tbl_like_comment'