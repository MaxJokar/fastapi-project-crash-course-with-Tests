from sqlalchemy.orm import Session
from item import models, schemas, database
from fastapi import HTTPException, status


def get_all(db: Session):
    items = db.query(models.Item).all()
    return items


def create(request: schemas.Item, db: Session):
    # return db
    # our scheme , need to use a model
    new_item = models.Item(
        item_name=request.item_name,
        item_brand=request.item_brand,
        price=request.price,
        buyer_id=1,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# ==========================================================================
def destroy(id: int, db: Session):
    del_item = db.query(models.Item).filter(models.Item.id == id)

    if not del_item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {del_item} not found",
        )
    del_item.delete(synchronize_session=False)
    db.commit()
    return "DONE:  Successfully Deleted"


def update(id: int, request: schemas.Item, db: Session):
    up_item_id = db.query(models.Item).filter(models.Item.id == id)

    if not up_item_id.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {up_item_id} not found",
        )
    up_item_id.update(request)
    up_item_id.commit()
    return "Updated"


# ==========================================================================


def show(id: int, db: Session):
    show_blog_id = db.query(models.Item).filter(models.Item.id == id).first()

    if not show_blog_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {show_blog_id} is not available",
        )
    return show_blog_id
