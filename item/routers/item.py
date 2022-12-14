from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from item import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from item.repository import item

# from item.routers import test_buyer

router = APIRouter(prefix="/Item", tags=["Items To buy "])
get_db = database.get_db


@router.get("/with Buyer's Information /", response_model=list[schemas.ShowItem])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.Item = Depends(oauth2.get_current_user),
):

    return item.get_all(db)
    # Refoactored : Reffer to => item.repository.item


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create(
    request: schemas.Item,
    db: Session = Depends(get_db),
    current_user: schemas.Item = Depends(oauth2.get_current_user),
):

    return item.create(request, db)
# ==========================================================================

@router.delete("/{id} ", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.Item = Depends(oauth2.get_current_user),
):

    return item.destroy(id, db)


@router.put("/{id} ", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Item,
    db: Session = Depends(get_db),
    current_user: schemas.Item = Depends(oauth2.get_current_user),
):

    return item.update(id, request, db)

# ==========================================================================
@router.get("/{id}", status_code=200, response_model=schemas.ShowItem)
def show(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.Item = Depends(oauth2.get_current_user),
):

    return item.show(id, db)
