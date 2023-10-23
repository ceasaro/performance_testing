import json

from django.core.management import BaseCommand

from core.db.mongo import MongoDB
from core.db.postgres import PostgresDB
from performance_testing.utils import elapsed_time

SENSOR_UUID = "d7f46f7a-5658-4c26-b80b-9b3a3dcfb6d3"


class Command(BaseCommand):
    help = "Management command for testing purposes."

    def add_arguments(self, parser) -> None:
        parser.add_argument("data_file_name", type=str)
        pass

    def handle(self, data_file_name, *args, **options):
        f = open(data_file_name, "r")

        # Reading from file
        json_data = json.loads(f.read())
        data = json_data.get("data")

        dbs_to_test = [MongoDB, PostgresDB]

        for db_class in dbs_to_test:
            db_instance = db_class()
            print(f"Clean all data in db {db_class}")
            db_instance.clean_data()

            print(f'Insert {len(data)} data entries into {db_class}.')
            duration = elapsed_time(db_instance.insert_data, data)
            print(f"Insertion took {duration} time")

            # print(f'Data in {db_class}:')
            # db_instance.print_data()
