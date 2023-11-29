import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://eli:z03kqfXTug2FhxqN@cluster0.1xtkxye.mongodb.net/?retryWrites=true&w=majority')

# Create a database
db: object = client["inventory"]

# Create a collection
collection: object = db["myCollection"]


def connect(name: str, picture: bytes, amount: int) -> None:
    """
    the fanc get the name and picture and int of amount and insert this into the database
    """
    d: object = {"name": name, 'picture': picture, 'amount': amount}

    collection.insert_one(d)


def show() -> object:
    """
    the func return the all date the in database
    \n
    -> return object :
    """
    data: object = collection.find().sort("name", -1)
    return data


def search(value: str) -> object:
    """
    the function get the value and search into the database and return the object
    :param value:
    :return:
    """
    data: object = collection.find({"name": value})
    return data


def update(name: str, value: int) -> None:
    """
    the function get the name and value and update the amount of item into the database
    :param name:
    :param value:
    :return:
    """
    collection.update_one(
        {"name": name},
        update={"$set": {"amount": value}}, )



