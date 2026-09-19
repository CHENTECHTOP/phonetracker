from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    model_name = models.CharField(max_length=100)
    imei_or_serial = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    custom_status = models.CharField(max_length=200, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.model_name} ({self.user.username})"


class RepairLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='repairs')
    action = models.CharField(max_length=200, verbose_name="Що зроблено")
    cost = models.IntegerField(verbose_name="Витрати (грн)")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} для {self.device.model_name}"