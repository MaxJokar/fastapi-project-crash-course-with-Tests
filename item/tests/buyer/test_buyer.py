"""
This is  a list of to Do  application & This one is for  "Buy groceries List" items.
This is API endpoint for creating an item ,updating or  Getting the item .
There are 4 test cases , we have 4 separate TEST cuz as soon as the application get bigger
its harder to  make test  a function individually.
"""
import requests
import pytest
from faker import Faker

# from conf_test_db import app
from main import app
import asyncio
from httpx import AsyncClient
import httpx


@pytest.mark.asyncio
async def test_post_buyer():
    fake = Faker()
    data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/buyer/test_buyer", json=data)

    assert response.status_code == 201
