import json
from datetime import datetime

from django.core.management import BaseCommand

from core.db.mongo import MongoDB
from core.db.postgres import PostgresDB
from core.management.commands.config import DATABASES_TO_TEST
from performance_testing.utils import elapsed_time, str_to_datetime, datetime_to_str

SENSOR_UUID = "d7f46f7a-5658-4c26-b80b-9b3a3dcfb6d3"


class Command(BaseCommand):
    help = "Management command for testing purposes."

    def add_arguments(self, parser) -> None:
        pass

    def handle(self, *args, **options):
        query = {
            'start': str_to_datetime("2023-01-01 00:00:00"),
            'end': str_to_datetime("2023-03-01 00:00:00"),
        }
        print(f"Query: {query}")
        for key, value in query.items():
            if isinstance(value, datetime):
                val = datetime_to_str(value)
            else:
                val = value

            print(f"   {key}: {val}")

        for db_class in DATABASES_TO_TEST:
            print(f"query performance testing {db_class}")
            db_instance = db_class()

            duration, resp = elapsed_time(db_instance.get_values, **query)
            print(f"count={len(resp)}")
            print(f"duration={duration}")

            # print(f'Data in {db_class}:')
            # db_instance.print_data()
            print('--------------------------------\n')
