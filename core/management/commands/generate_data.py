import json

from django.core.management import BaseCommand

from core.generate_data import generate_data
from performance_testing.utils import str_to_datetime

SENSOR_UUID = "d7f46f7a-5658-4c26-b80b-9b3a3dcfb6d3"


class Command(BaseCommand):
    help = "Management command for testing purposes."

    def add_arguments(self, parser) -> None:
        parser.add_argument("-m", "--measurements", type=int)
        pass

    def handle(self, measurements, *args, **options):
        sensor_uuid_count = 3
        start_date = str_to_datetime("2023-01-01 00:00:00")
        data_entries = generate_data(measurements, sensor_uuid_count, start_date)
        print(json.dumps({"data": data_entries}))
