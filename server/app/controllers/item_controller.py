from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from app.services.item_service import get_all_items, get_item, create_item, update_item, delete_item

item_controller = Blueprint('item_controller', __name__)

@jwt_required()
def get_all():
    items = get_all_items()
    return jsonify({'items': [item.to_dict() for item in items]})

@jwt_required()
def get_by_id(item_id):
    item = get_item(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'found_item': item.to_dict()})

@jwt_required()
def create():
    payload = request.get_json()
    item_to_create = create_item(payload)
    return jsonify({'message': 'Item created', 'created_item': item_to_create.to_dict()}), 201

@jwt_required()
def update(item_id):
    payload = request.get_json()
    item_to_update = update_item(item_id, payload)
    if item_to_update is None:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'message': 'Item updated', 'updated_item': item_to_update.to_dict()})

@jwt_required()
def delete(item_id):
    item = delete_item(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    return '', 204
