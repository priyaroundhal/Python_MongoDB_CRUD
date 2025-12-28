def update_user(db):
    name= input("enter name to update: ")
    role=input("enter new role: ")

    result=db.users.update_one({"name": name}, {"$set": {"role":role}})

    if result.modified_count:
        print("user updated")
    else:
        print("user not updated")