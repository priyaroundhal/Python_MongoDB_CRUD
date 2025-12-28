def create_user(db):
    name= input("enter Name: ")
    role= input("enter role: ")
    experience= input("enter experience: ")

    user={"name":name, "role": role, "experience":experience}
    result=db.users.insert_one(user)

    print("user created with id",result.inserted_id)
