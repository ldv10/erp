from playhouse.shortcuts import model_to_dict

import erp_app.db.models as models
from erp_app.app import app
from flask import jsonify


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
