from playhouse.shortcuts import model_to_dict

from erp_app.db.models import Client


def get_all_clients():
    query = (
        Client
        .select()
    )

    return [ 
        model_to_dict(client, only=[
            Client.id,
            Client.name,
            Client.number,
            Client.address,
            Client.nit
        ])
        for client in query 
    ]