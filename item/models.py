from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from item.database import Base


class Item(Base):
    __tablename__ = "items"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    item_brand = Column(String)
    price = Column(Integer)
    buyer = relationship("Buyer", back_populates="items")
    buyer_id = Column(Integer, ForeignKey("buyers.id"))


class Buyer(Base):
    __tablename__ = "buyers"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("Item", back_populates="buyer")
