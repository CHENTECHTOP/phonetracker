from django.db import models


class Device(models.Model):
    STATUS_CHOICES = [
        ('in_repair', 'На діагностиці / В ремонті'),
        ('ready', 'Готовий до продажу'),
        ('sold', 'Продано'),
    ]
    model_name = models.CharField(max_length=100, verbose_name="Модель (напр. iPhone 11 Pro)")
    imei_or_serial = models.CharField(max_length=50, unique=True, verbose_name="IMEI / Серійник")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_repair')
    custom_status = models.CharField(max_length=100, blank=True, default='', verbose_name="Кастомний стан")
    purchase_price = models.IntegerField(verbose_name="Ціна покупки (грн)")

    def __str__(self):
        return f"{self.model_name} - {self.get_status_display()}"


class RepairLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='repairs')
    action = models.CharField(max_length=200, verbose_name="Що зроблено")
    cost = models.IntegerField(verbose_name="Витрати (грн)")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} для {self.device.model_name}"