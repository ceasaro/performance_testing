import pymongo

from django.conf import settings

from core.db.base import AbstractPerformanceTestDb
from performance_testing.utils import timestamp_to_datetime


class MongoDB(AbstractPerformanceTestDb):

    def __init__(self) -> None:
        mongodb_client = pymongo.MongoClient(
            host=settings.MONGO_DB.get("HOST"),
            port=settings.MONGO_DB.get("PORT"),
            username=settings.MONGO_DB.get("USERNAME"),
            password=settings.MONGO_DB.get("PASSWORD"),
            authsource=settings.MONGO_DB.get("AUTHSOURCE"),
            uuidRepresentation="standard",
        )

        self.database = mongodb_client.get_database(settings.MONGO_DB.get("DB_NAME"))
        self.collection = self.database.get_collection("perf_collection")
        self.collection.create_index(
            [("timestamp", pymongo.DESCENDING), ("sensor_uuid", pymongo.ASCENDING)],
            unique=True
        )

    def clean_data(self):
        return self.collection.drop()

    def insert_data(self, data):
        for item in data:
            self.collection.insert_one({
                'timestamp': timestamp_to_datetime(item.get('timestamp')),
                'sensor_uuid': item.get('sensor_uuid'),
                'value': item.get('value'),
                'origin_value': item.get('origin_value'),
            })

    def print_data(self):
        for document in self.collection.find():
            print(document)
