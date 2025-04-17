from typing import List
from sqlalchemy import Integer, String, ForeignKey, event
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    haslo: Mapped[str] = mapped_column(String(120))

    def __init__(self, login=None, haslo=None):
        self.login = login
        self.haslo = haslo

    def __repr__(self):
        return f'<User {self.login!r}>'

@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(User(login='adam', haslo='adam@domain.com'))
    db.session.commit()

class Pytanie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pytanie: Mapped[str] = mapped_column(String(255), unique=True)
    odpok: Mapped[str] = mapped_column(String(100))
    odpowiedzi: Mapped[List['Odpowiedz']] = relationship(
        'Odpowiedz', back_populates='pytanie',
        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.pytanie

class Odpowiedz(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pytanie_id: Mapped[int] = mapped_column(ForeignKey('pytanie.id', ondelete="CASCADE"))
    pytanie: Mapped['Pytanie'] = relationship("Pytanie", back_populates="odpowiedzi")
    odpowiedz: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return self.odpowiedz
