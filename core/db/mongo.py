import pymongo

from django.conf import settings

from core.db.base import AbstractPerformanceTestDb
from performance_testing.utils import timestamp_to_datetime


class MongoDB(AbstractPerformanceTestDb):

    def __init__(self) -> None:
        self.mongodb_client = pymongo.MongoClient(
            host=settings.MONGO_DB.get("HOST"),
            port=settings.MONGO_DB.get("PORT"),
            username=settings.MONGO_DB.get("USERNAME"),
            password=settings.MONGO_DB.get("PASSWORD"),
            authsource=settings.MONGO_DB.get("AUTHSOURCE"),
            uuidRepresentation="standard",
        )

        self.database = self.mongodb_client.get_database(settings.MONGO_DB.get("DB_NAME"))
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

    def get_values(self, sensor_uuid=None, start=None, end=None, sort=False):
        query = self._query_filter(sensor_uuid, start, end)
        measurements_data = self.collection.find(query)
        if sort:
            print("SORTING BY DATE")
            measurements_data.sort("timestamp", pymongo.DESCENDING)

        return [m.get('value') for m in measurements_data]

    def aggregate_per_day(self, sensor_uuid=None, start=None, end=None, sort=False):
        query = self._query_filter(sensor_uuid, start, end)

        aggregated_data = self.collection.aggregate([
            {"$match": query},
            {"$addFields": {"day": {"$dayOfYear": "$timestamp"}}},
            {"$group": {
                "_id": "$day",
                "daily_sum": {"$sum": "$value"}
            }}
        ])
        return [m for m in aggregated_data]

    def print_data(self):
        for document in self.collection.find():
            print(document)

    def _query_filter(self, sensor_uuid=None, start=None, end=None):
        query = {}
        if sensor_uuid:
            query["sensor_uuid"] = sensor_uuid
        timestamp_filter = {}
        if start:
            timestamp_filter["$gte"] = start
        if end:
            timestamp_filter["$lte"] = end
        if timestamp_filter:
            query["timestamp"] = timestamp_filter
        return query
