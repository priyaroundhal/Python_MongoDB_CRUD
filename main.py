from db.mongo_connection import get_database
from crud.create import create_user
from crud.read_user import read_user
from crud.update_user import update_user
from crud.delete_user import delete_user

db= get_database()

while True:
    print("\n1. Create User")
    print("\n2. Read User")
    print("3. Update User")
    print("4. Delete User")
    print("\n5. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        create_user(db)
    elif choice == "2":
        read_user(db)
    elif choice == "3":
        update_user(db)
    elif choice == "4":
        delete_user(db)
    elif choice == "5":
        print("exiting application")
        break

    else:
        print("wrong choice")
