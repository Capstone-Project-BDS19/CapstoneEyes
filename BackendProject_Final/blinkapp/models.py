from django.db import models
from django.conf import settings

# Create your models here.

class blnk(models.Model):
    #uID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    user = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    blink_rate = models.IntegerField()
    strain_cnt = models.IntegerField()
    drowsy_cnt = models.IntegerField()
    

    class Meta:
        db_table = 'blnk'