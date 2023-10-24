from core.db.mongo import MongoDB
from core.db.postgres import PostgresDB

DATABASES_TO_TEST = [MongoDB, PostgresDB]
