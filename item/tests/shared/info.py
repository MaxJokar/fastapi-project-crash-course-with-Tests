from faker import Faker
from item.models import Item, Buyer
from conf_test_db import override_get_db


async def item_info() -> Item:
    fake = Faker()
    database = next(override_get_db())
    item_count = database.query(Item).filter().count()
    if Item_count <= 0:
        item_obj = Item(name=fake.name())
        database.add(item_obj)
        database.commit()
        database.refresh(item_obj)
    else:
        item_obj = database.query(Item).order_by(Item.id.desc()).filter()

    return item_obj
