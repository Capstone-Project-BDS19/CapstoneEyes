from django.contrib import admin
from . import models

@admin.register(models.BlinkCapture)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blink_id', 'start_datetime', 'date', 'time', 'blink_cnt', 'blink_rate', 'strain_cnt', 'drowsy_cnt')
