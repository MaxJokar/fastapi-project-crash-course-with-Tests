from sqlalchemy.orm import Session
from item import models, schemas, database
from fastapi import HTTPException, status

# from item.hashing import Hash
ENDPOINT = "http://localhost:8000/docs"
# ENDPOINT = "http://localhost:8000/docs"


def get_all(db: Session):
    blogs = db.query(models.Buyer).all()
    # assert blogs.status_code == 200

    return blogs


def create(request: schemas.Buyer, db: Session):

    new_buyer = models.Buyer(
        name=request.name,
        email=request.email,
        password=request.password,
        # password=Hash.bcrypt(request.password),
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return new_buyer


def show(id: int, db: Session):
    new_buyer = db.query(models.Buyer).filter(models.Buyer.id == id).first()
    if not new_buyer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Buyer with id {id} not available",
        )
    return new_buyer