from fastapi.encoders import jsonable_encoder
from typing import List
from app.schema import Farmer, FarmerUpdate, Purchase, Review


def hash_name(name):
    return sum(map(ord, name)) % 2


def find_database_with_farmer(database_list, id: str):
    for db in database_list:
        if db["farmers"].find_one({"_id": id}):
            return db
    return None


def create_farmer_db(database_list, farmer: Farmer):
    database = database_list[hash_name(farmer.dict().get('name'))]
    farmer = jsonable_encoder(farmer)
    new_farmer = database["farmers"].insert_one(farmer)
    return database["farmers"].find_one({"_id": new_farmer.inserted_id})


def list_farmers_db(database_list) -> List[Farmer]:
    return list(database_list[0]["farmers"].find()) + list(database_list[1]["farmers"].find())


def find_farmer_db(database_list, id: str) -> Farmer:
    for db in database_list:
        farmer = db["farmers"].find_one({"_id": id})
        if farmer:
            return farmer
    return None


def update_farmer_db(database_list, id: str, farmer: FarmerUpdate):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return None
    current_farmer = db["farmers"].find_one({"_id": id})
    update_data = {k: v for k, v in farmer.dict().items() if v is not None}
    if 'product_list' in update_data:
        new_product_list = update_data['product_list']
        current_product_list = current_farmer.get('product_list')
        if current_product_list is None:
            current_product_list = dict()
        for product_name, product_info in new_product_list.items():
            current_product_list[product_name] = product_info
        update_data['product_list'] = current_product_list
    db["farmers"].update_one({"_id": id}, {"$set": update_data})
    return db["farmers"].find_one({"_id": id})


def delete_farmer_db(database_list, id: str):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return 0
    return db["farmers"].delete_one({"_id": id}).deleted_count


def delete_product_db(database_list, id: str, product_name: str):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return 0
    update_result = db["farmers"].update_one(
        {"_id": id},
        {"$unset": {f"product_list.{product_name}": ""}}
    )
    return update_result.modified_count


def list_farmers_by_product_db(database_list, product_name: str) -> List[Farmer]:
    pipeline = [
        {"$match": {f"product_list.{product_name}": {"$exists": "true"}}},
        {"$project": {"name": 1, "contact": 1, "location": 1, f"product_list.{product_name}": 1}}
    ]
    return list(database_list[0]["farmers"].aggregate(pipeline)) + list(database_list[1]["farmers"].aggregate(pipeline))


def purchase_product_db(database_list, id: str, product_name: str, purchase: Purchase):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return None
    key = f"product_list.{product_name}.inventory"
    current_inventory = db["farmers"].find_one({"_id": id}, {"inventory": "$" + key})
    new_inventory = current_inventory.get("inventory") - purchase.dict().get("quantity")
    db["farmers"].update_one({"_id": id}, {"$set": {key: new_inventory}})
    return db["farmers"].find_one({"_id": id}, {"name": 1, "contact": 1, "location": 1, f"product_list.{product_name}": 1})


def review_product_db(database_list, id: str, product_name: str, review: Review):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return None
    key = f"product_list.{product_name}"
    current_review_count = db["farmers"].find_one({"_id": id}, {"review_count": "$" + key + ".review_count"}).get("review_count")
    current_rating = db["farmers"].find_one({"_id": id}, {"rating": "$" + key + ".rating"}).get("rating")
    new_review_count = current_review_count + 1
    if current_review_count == 0:
        new_rating = review.dict().get("rating")
    else:
        new_rating = (current_rating * current_review_count + review.dict().get("rating")) / new_review_count
    db["farmers"].update_one({"_id": id}, {"$set": {key + ".rating": new_rating}})
    db["farmers"].update_one({"_id": id}, {"$set": {key + ".review_count": new_review_count}})
    return db["farmers"].find_one({"_id": id}, {"name": 1, "contact": 1, "location": 1, f"product_list.{product_name}": 1})
