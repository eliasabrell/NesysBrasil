from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class DailyAccess(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    data = models.DateField(default=now)

    class Meta:
        unique_together = ('username', 'ip_address', 'data')
