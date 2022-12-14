from fastapi import APIRouter, Depends, status
from item import database, schemas, models, oauth2
from sqlalchemy.orm import Session

from ..hashing import Hash
from item.repository import buyer

router = APIRouter(prefix="/Buyer", tags=["Buyers"])
get_db = database.get_db


@router.get("/", response_model=list[schemas.ShowBuyer])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.Buyer = Depends(oauth2.get_current_user),
):

    return buyer.get_all(db)


# Refacterred : go to repository buyer.py  for continue


@router.post("/", response_model=schemas.ShowBuyer)
def create_buyer(request: schemas.Buyer, db: Session = Depends(get_db)):
    return buyer.create(request, db)
    # Refacterred : go to repository buyer.py  for continue


@router.get("/{id} ", response_model=schemas.ShowBuyer)
def get_buyer(id: int, db: Session = Depends(get_db)):
    return buyer.show(id, db)


# Refacterred : go to repository buyer.py  for continue
