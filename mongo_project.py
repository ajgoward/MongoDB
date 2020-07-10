import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a Record")
    print("2. Find a Record by name")
    print("3. Edit a Record")
    print("4. Delete a Record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have slected option 2")
        elif option == "3":
            print("You have slected option 3")
        elif option == "4":
            print("You have slected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid Option")
        print("")


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
