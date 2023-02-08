from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from convector import configur
from models import BatchRequestSchema

bp_pars = Blueprint('main', __name__, url_prefix='/perform_query')


@bp_pars.route('/', methods=['POST'])
def post():
    req = request.json
    try:
        val_data = BatchRequestSchema().load(req)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in val_data['queries']:
        result = configur(
            cmd=query['cmd'],
            value=query['value'],
            file_name=val_data['file_name'],
            data=result
        )
    return jsonify(result)
