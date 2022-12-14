# """
# This is  a list of to Do  application & This one is for  "Buy groceries List" items.
# This is API endpoint for creating an item ,updating or  Getting the item .
# There are 4 test cases , we have 4 separate TEST cuz as soon as the application get bigger
# its harder to  make test  a function individually.
# """
# import requests

# # universally unique identifier: To produce new  user_id  & content:refer to "new_task_payload"
# import uuid


# # ENDPOINT = "http://localhost:8000/docs"
# ENDPOINT = "https://todo.pixegami.io/"

import requests
import pytest
from item.models import Buyer, Item

# from conf_test_db import app
from main import app
import asyncio
from httpx import AsyncClient
import httpx
from conf_test_db import override_get_db


@pytest.mark.asyncio
async def test_new_item():

    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/item/test_item", json={"name": "tea"})
    assert response.status_code == 201
    assert response.json()["name"] == ["tea"]


@pytest.mark.asyncio
async def test_list_get_item():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_item = Item(
            item_name="pasta", item_brand="ItalianPasta", price=2, buyer="clienA"
        )
        database.add(new_item)
        database.commit()
        database.refresh(new_item)
        first_response = await ac.get("/item/test_item")
        second_response = await ac.get(f"/item/test_item/{new_item.id}")

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert second_response.json() == {
        "id": new_item.id,
        "name": new_item.name,
        "item_brand": new_item.brand,
        "price": new_item.price,
        "buyer": new_item.buyer,
    }


@pytest.mark.asyncio
async def test_delete_item():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_item = Item(
            item_name="pasta", item_brand="ItalianPasta", price=2, buyer="clienA"
        )
        database.add(new_item)
        database.commit()
        database.refresh(new_item)
        response = await ac.delete(f"/item/test_item/{new_item.id}")
    assert (
        response.status_code == 204
    )  # request has succeded ,no need to navigate from current page
