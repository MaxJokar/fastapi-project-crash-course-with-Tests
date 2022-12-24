from fastapi import APIRouter, Depends, status, HTTPException
from item import schemas, database, models, token
from sqlalchemy.orm import Session

from item.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):

    buyer = db.query(models.buyer).filter(models.buyer.email == request.buyername).first()
    if not buyer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hash.verify(buyer.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password "
        )

    access_token = token.create_access_token(data={"sub": buyer.email})
    return {"access_token": access_token, "token_type": "bearer"}

    # generate a jwt token and return
    return buyer
