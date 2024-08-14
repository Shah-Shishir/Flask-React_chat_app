from app.models import db, Item
from sqlalchemy.exc import NoResultFound

def get_all_items():
    return Item.query.all()

def get_item(item_id):
    try:
        return Item.query.filter_by(id=item_id).first()
    except NoResultFound:
        return None

def create_item(data):
    item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(item)
    db.session.commit()
    return item

def update_item(item_id, data):
    item = get_item(item_id)
    if item is None:
        return None

    if 'name' in data:
        item.name = data['name']
    if 'description' in data:
        item.description = data['description']

    db.session.commit()
    return item

def delete_item(item_id):
    item = get_item(item_id)
    if item is None:
        return None

    db.session.delete(item)
    db.session.commit()
    return item
