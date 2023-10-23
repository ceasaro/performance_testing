import random
import uuid
from datetime import timedelta, datetime


def generate_data(measurement_count, sensor_uuid_count, start_date):
    sensor_uuids = [uuid.uuid4() for i in range(sensor_uuid_count)]
    hour_count = int(measurement_count / sensor_uuid_count)+1
    data_entries = []
    for single_date in (start_date + timedelta(hours=h) for h in range(hour_count)):
        for sensor_uuid in sensor_uuids:
            value = int(random.uniform(0, 100))
            data_entries.append({
                'sensor_uuid': str(sensor_uuid),
                'value': value,
                'timestamp': datetime.timestamp(single_date),
                'origin_value': value,
            })
            measurement_count -= 1
            if measurement_count <= 0:
                return data_entries
    return data_entries
