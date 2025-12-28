def delete_user(db):
    name= input("enter name to delete: ")

    result =db.users.delete_one({"name":name})
    if result.deleted_count:
        print("user deleted")
    else:
        print("user not found")