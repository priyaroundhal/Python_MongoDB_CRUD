def read_user(db):
    users= db.users.find()

    for users in users:
        print(users)