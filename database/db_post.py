"""
This is a DAO file, an abstraction of PostgreSQL Operations and API end-points.
"""
from fastapi import HTTPException, status
from router.schemas import PostBase,PostDisplay
from sqlalchemy.orm.session import Session
from datetime import datetime
from database.models import DbPost
from typing import List


def create(db: Session, request: PostBase):
    """
    This functions creates post and writes post information in the database
    :param db: DBI session
    :param request: Payload
    :return:  class (payload) after inserting the same payload
    """
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session) -> List[PostDisplay]:
    """
    This function is used to fetch all posts from database.
    :param db: DBI session
    :return: List of all posts
    """
    return db.query(DbPost).all()


def delete(db: Session, id_: int, ) -> str:
    """
    This function is used to delete posts based on id
    :param db: DBI session
    :param id_: post id
    :return: string with ok message
    """
    post = db.query(DbPost).filter(DbPost.id == int(id_)).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id_} not found")
    db.delete(post)
    db.commit()
    return 'ok'
