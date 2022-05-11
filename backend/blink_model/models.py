from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class BlinkCapture(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete= models.CASCADE,
        related_name = 'blink_capture'
    )
    blink_id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField(default = timezone.now)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    blink_cnt = models.IntegerField()
    blink_rate = models.IntegerField()
    strain_cnt = models.IntegerField()
    drowsy_cnt = models.IntegerField()

    class Meta:
        unique_together = (('user', 'blink_id'))

    def __str__(self):
        return (self.user, self.blink_id)
