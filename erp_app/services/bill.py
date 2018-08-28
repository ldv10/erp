from playhouse.shortcuts import model_to_dict

from erp_app.db.models import Bill


def get_all_clients():
    query = (
        Bill
        .select()
    )

    return [ 
        model_to_dict(bill, only=[
            Bill.id,
            Bill.client_id,
            Bill.total,
            Bill.emission_date,
            Bill.payment
        ])
        for bill in query 
    ]