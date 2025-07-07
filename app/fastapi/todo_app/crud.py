import logging
import random
import time

from sqlalchemy.orm import Session

from . import models, schemas


def get_todo(db: Session, todo_id: int) -> models.TodoItem:
    # Simulate a slow query
    logging.error(f"Slow query for todo: {todo_id}")
    time.sleep(1)
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()


def get_todo_list(db: Session, skip: int = 0, limit: int = 10) -> list[models.TodoItem]:
    return db.query(models.TodoItem).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate) -> models.TodoItem:
    todo_item = models.TodoItem(**todo.model_dump())
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item


def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate) -> models.TodoItem:
    todo_item = (
        db.query(models.TodoItem)
        .filter(models.TodoItem.id == todo_id)
        .with_for_update()
        .first()
    )
    if todo_item is None:
        return None
    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo_item, key, value)
    if random.random() > 0.9:
        time.sleep(1)
        logging.error(f"Slow update for todo: {todo_id}")
    db.commit()
    return todo_item


def delete_todo(db: Session, todo_id: int) -> models.TodoItem:
    todo_item = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if todo_item is None:
        return None
    db.delete(todo_item)
    db.commit()
    return todo_item


def slow_update_todo(db: Session, todo_id: int) -> str:
    todo_item = (
        db.query(models.TodoItem)
        .filter(models.TodoItem.id == todo_id)
        .with_for_update()
        .one()
    )
    # Perform some operations on the locked row
    todo_item.title = "Updated Title"
    # Commit the transaction
    db.commit()
