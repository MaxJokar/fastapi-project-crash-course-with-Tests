"""
The Item refers to  Products for sale and Buyer as our Regular Customer/Customers we
are collecting Data about Our Customer's data (name, email etc) &the Products their Purchase
such as : name,brand, price etc.manually or as a group in Swagger visible their datas.

"""

from fastapi import FastAPI
from item.database import engine
from item.routers import item, buyer, authentication
from item import models


app = FastAPI()
# create all the models into DB(table)
# (table or migrate all tables  in our  database table)
models.Base.metadata.create_all(engine)

#  desplay separately on Swagger UI
app.include_router(authentication.router)
app.include_router(item.router)
app.include_router(buyer.router)
