from playhouse.shortcuts import model_to_dict

from erp_app.db.models import User


def verify_login(data):
    name = data.get('name', '')
    password = data.get('password', '')
    user_type = data.get('type', '')

    query = (
        User
        .select()
        .where(
            User.name == name,
            User.password == password,
            User.type == user_type
        )
    )

    print(query)

    return model_to_dict(query.get())