from sqlalchemy.orm import Session
from . import models

def create_guest(db: Session, name: str, email: str, phone: str):
    guest = models.Guest(name=name, email=email, phone=phone)
    db.add(guest)
    db.commit()
    db.refresh(guest)
    return guest

def get_guests(db: Session):
    return db.query(models.Guest).all()