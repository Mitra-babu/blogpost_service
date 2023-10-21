import shutil

from fastapi import APIRouter, Depends, UploadFile, File
from router.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_post
import string, random
from datetime import datetime

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


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    random_str = ''.join(random.choice(letter) for i in range(6))
    random_str += str(datetime.now().microsecond)
    filename = f'{random_str}'.join(image.filename.rsplit(".", 1))
    path = f'images/{filename}'
    with open(path, "w+b") as file:
        shutil.copyfileobj(image.file, file)
    return {'filename': path}
