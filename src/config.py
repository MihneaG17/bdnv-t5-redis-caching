import os

import redis
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]
MONGO_DB = os.getenv("MONGO_DB", "sample_airbnb")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "listingsAndReviews")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "300"))


def get_mongo_collection():
    client = MongoClient(MONGO_URI)
    return client[MONGO_DB][MONGO_COLLECTION]


def get_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
