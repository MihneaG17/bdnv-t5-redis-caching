import json
import time

from config import CACHE_TTL_SECONDS, get_mongo_collection, get_redis

r = get_redis()
listings = get_mongo_collection()

PROIECTIE = {
    "name": 1,
    "property_type": 1,
    "price": 1,
    "accommodates": 1,
    "address.market": 1,
    "review_scores.review_scores_rating": 1,
}

stats = {"hit": 0, "miss": 0}


def get_listing(listing_id: str):
    key = f"listing:{listing_id}"

    cached = r.get(key)
    if cached is not None:
        stats["hit"] += 1
        return json.loads(cached)

    stats["miss"] += 1
    doc = listings.find_one({"_id": listing_id}, PROIECTIE)
    if doc is None:
        return None

    r.set(key, json.dumps(doc, default=str), ex=CACHE_TTL_SECONDS)
    return doc


def timp_mediu_ms(ids):
    start = time.perf_counter()
    for i in ids:
        get_listing(i)
    return (time.perf_counter() - start) / len(ids) * 1000


if __name__ == "__main__":
    ids = [d["_id"] for d in listings.find({"address.market": "Porto"}, {"_id": 1}).limit(20)]

    r.delete(*[f"listing:{i}" for i in ids])

    rece = timp_mediu_ms(ids)
    cald = timp_mediu_ms(ids)

    print(f"Prima trecere  (cache gol,  MISS): {rece:8.2f} ms / anunț")
    print(f"A doua trecere (cache plin, HIT):  {cald:8.2f} ms / anunț")
    print(f"Accelerare: de {rece / cald:.0f} ori mai rapid")
    total = stats["hit"] + stats["miss"]
    print(f"Hit rate: {stats['hit']}/{total} = {stats['hit'] / total:.0%}")

    exemplu = f"listing:{ids[0]}"
    print(f"\nCheia {exemplu} expiră în {r.ttl(exemplu)} secunde (TTL)")
    print("Conținut:", r.get(exemplu))
