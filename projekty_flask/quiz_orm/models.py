from app import db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

class Pytanie(db.Model):
    id = Column(Integer, primary_key=True)
    pytanie = Column(String(255), unique=True)
    odpok = Column(String(100))
    odpowiedzi = relationship(
        'Odpowiedz', back_populates='pytanie',
        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.pytanie

class Odpowiedz(db.Model):
    id = Column(Integer, primary_key=True)
    pytanie_id = Column(Integer, ForeignKey('pytanie.id', ondelete="CASCADE"))
    pytanie = relationship("Pytanie", back_populates="odpowiedzi")
    odpowiedz = Column(String(100))

    def __repr__(self):
        return self.odpowiedz
