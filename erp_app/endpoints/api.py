from playhouse.shortcuts import model_to_dict

import erp_app.db.models as models
import erp_app.services.auth as auth
import erp_app.services.client as client
from erp_app.app import app
from flask import jsonify, request


@app.route('/')
def hello_world():
    return 'ERP APP'


@app.route('/cuopon/<int:id>')
def cuopon_route(id):
    response = (
        models
        .Cuopon
        .get(models.Cuopon.cuopon == id)
    )

    return jsonify(model_to_dict(response))

@app.route('/auth')
def auth_route():
    data = request.args.to_dict()
    return jsonify(auth.verify_login(data))

@app.route('/clients')
def clients_route():
    return jsonify(client.get_all_clients())

@app.route('/bill')
def bill_route():
    return 'Working on bills...'
