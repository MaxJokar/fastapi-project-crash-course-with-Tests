# a for pydantic model called  schema
"""
A schema is used to validate data we receive as well as to reformat
the data that we want to send to the client/browser.
"""
from pydantic import BaseModel
from typing import List, Optional


from item.models import Buyer, Item


class ItemBase(BaseModel):
    item_name: str
    item_brand: str
    price: int


class Item(ItemBase):
    class Config:
        orm_mode = True


class Buyer(BaseModel):
    name: str
    email: str
    password: str


class ShowBuyer(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


# To show the relationship  Buyer creator & Item together (buyer:showbuyer)
class ShowItem(BaseModel):
    item_name: str
    item_brand: str
    buyer: ShowBuyer

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
