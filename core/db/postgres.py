from core.db.base import AbstractPerformanceTestDb
from core.models import Measurement
from performance_testing.utils import timestamp_to_datetime


class PostgresDB(AbstractPerformanceTestDb):

    def __init__(self) -> None:
        self.db_name = 'postgres'

    def clean_data(self):
        return Measurement.objects.using(self.db_name).delete()

    def insert_data(self, data):
        measurements = []
        for item in data:
            measurements.append(Measurement(
                timestamp=timestamp_to_datetime(item.get('timestamp')),
                sensor_uuid=item.get('sensor_uuid'),
                value=item.get('value'),
                origin_value=item.get('origin_value'),
            ))

        Measurement.objects.using(self.db_name).bulk_create(measurements)

    def print_data(self):
        for m in Measurement.objects.using(self.db_name):
            print(m)

