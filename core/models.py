from django.db import models


class Measurement(models.Model):
    timestamp = models.DateTimeField()
    sensor_uuid = models.CharField(max_length=256)
    value = models.FloatField()
    origin_value = models.FloatField()

    class Meta:
        ordering = ["timestamp"]
        unique_together = ("sensor_uuid", "timestamp")
        index_together = [["sensor_uuid", "timestamp"]]
