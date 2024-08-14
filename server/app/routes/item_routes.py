from flask import Blueprint
from app.controllers import item_controller

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/items', methods=['GET'])
def get_items():
    return item_controller.get_all()

@item_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return item_controller.get_by_id(item_id)

@item_bp.route('/items', methods=['POST'])
def create_item():
    return item_controller.create()

@item_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return item_controller.update(item_id)

@item_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return item_controller.delete(item_id)
