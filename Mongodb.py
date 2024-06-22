from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["curd_app_db"]
collections = db["items"]


def create_item(name, description, price):
    item = {"name": name, "description": description, "price": price}
    collections.insert_one(item)
    print("Item Added")


def read_items():
    items = collections.find()
    for item in items:
        print(item)


def update_item(name, new_values):
    query = {"name": name}
    new_data = {"$set": new_values}
    collections.update_one(query, new_data)
    print(f"item {name} updated")


def delete_item(name):
    query = {"name": name}
    collections.delete_one(query)
    print(f"item {name} Deleted")


def average_price():
    pipeline = [{
        "$group":
            {
                "_id": None,
                "average_price": {"$avg": "$price"},
                "sum": {"$sum": "$price"},
            }
    }]

    result = collections.aggregate(pipeline)
    for data in result:
        print(data)


def create_index():
    index_name = collections.create_index([("name",1)])
    print(f"Index Created {index_name}")

if __name__ == "__main__":
    #    create_item("Shampoo","Hair Product", 1200)
    #    create_item("Conditioner","Hair Product", 1600)
    #    update_item("Shampoo", {"price":1500})
    #    delete_item("Conditioner")

    create_index()
    read_items()
    average_price()
