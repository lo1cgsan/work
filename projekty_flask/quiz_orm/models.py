from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

class Pytanie(Base):
    id = Column(baza.Integer, primary_key=True)
    pytanie = Column(Unicode(255), unique=True)
    odpok = Column(Unicode(100))
    odpowiedzi = relationship(
        'Odpowiedz', backref=baza.backref('pytanie'),
        cascade="all, delete, delete-orphan")

    def __str__(self):
        return self.pytanie


class Odpowiedz(baza.Model):
    id = baza.Column(baza.Integer, primary_key=True)
    pnr = baza.Column(baza.Integer, baza.ForeignKey('pytanie.id'))
    odpowiedz = baza.Column(baza.Unicode(100))

    def __str__(self):
        return self.odpowiedz
