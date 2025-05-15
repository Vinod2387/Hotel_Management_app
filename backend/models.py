from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base

class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    room_number = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)