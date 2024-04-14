from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    is_view = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='tbl_notification'
