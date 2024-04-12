from django.db import models
from user.models import User

# Create your models here.
class Conversation(models.Model):
    user_send = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send')
    user_receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive')
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tbl_conversation'