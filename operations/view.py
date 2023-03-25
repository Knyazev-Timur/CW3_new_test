from flask import Blueprint, render_template, request, jsonify
from utils import read_json

operations_blueprint = Blueprint('operations_blueprint', __name__, template_folder='templates', url_prefix='/')

@operations_blueprint.route('/')
def page_index():
    all_operations = read_json('./data/operations.json')
    return jsonify(all_operations)
