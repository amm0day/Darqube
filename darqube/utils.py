from pymongo import MongoClient
from .settings import DATABASES


CLIENT_PARAMS = {k.lower(): v for k, v in DATABASES["default"].items()}
CLIENT_PARAMS.pop("engine")
DB_NAME = CLIENT_PARAMS.pop("name")

def get_db_handle():
    client = MongoClient(**CLIENT_PARAMS)
    db_handle = client[DB_NAME]
    return db_handle, client

def get_collection_handle(collection_name):
    db_handle, _ = get_db_handle()
    return db_handle[collection_name]
