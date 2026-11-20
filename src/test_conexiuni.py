from config import get_mongo_collection, get_redis

r = get_redis()
r.ping()
print("Redis OK")

listings = get_mongo_collection()
total = listings.count_documents({})
porto = listings.count_documents({"address.market": "Porto"})
print(f"MongoDB OK: {total} anunțuri în total, dintre care {porto} din Porto")

exemplu = listings.find_one({"address.market": "Porto"}, {"name": 1, "price": 1})
print("Exemplu de anunț:", exemplu)
