from django.db import models
from django.utils import timezone
from datetime import datetime

class TaskModel(models.Model):
    task = models.CharField(
        verbose_name="Формулировка задачи",
        default="Дано вещественное число A. Вычислить x = a**4, при a < 10; x = a при a > 61, в противном случае x  = a − sin(a**2)).",
        max_length=255,
    )
    a = models.FloatField(
        verbose_name="Значение А",
        default=0,
    )
    result = models.FloatField(
        verbose_name="Результат",
        default=0,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)",
        default=datetime.now(tz=timezone.utc),
    )

    def __str__(self):
        return f"{self.id}&{self.task}"

    class Meta:
        verbose_name = "Таблица задачи"
        verbose_name_plural = "Таблицы задачи"
        ordering = ("-id", "-a")
