from fastapi import APIRouter, Depends
from router.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_post

router = APIRouter(prefix="/post", tags=["Post"])


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete('/{id_}')
def delete(id_: int, db: Session = Depends(get_db)):
    return db_post.delete(db, id_)
