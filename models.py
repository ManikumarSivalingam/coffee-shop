"""Models for the coffee-shop application: SQLAlchemy ORM model definitions."""

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
meta = MetaData()

"""User model representing users in the coffee-shop application.""" 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    def __repr__(self):
        return f"User({self.id}, '{self.firstname}', '{self.lastname}', '{self.email}')"
    
class Thing(Base):
    """Thing model representing items owned by users in the coffee-shop application."""
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    owner = Column(Integer, ForeignKey('users.id'), nullable=True)

    def __init__(self, id,  name, description, owner):
        self.id = id
        self.name = name
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"Thing({self.id}, '{self.name}', '{self.description}', {self.owner})"

engine = create_engine("sqlitecloud://cp2dejwkvz.g5.sqlite.cloud:8860/coffee-shop?apikey=A0eyHwO1z6rgD77c5tRAZyb1bZ8LvJ75Vmlrnc9saAY")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# u1 = User("Jane", "Smith", "jane.smith@example.com", "anotherpassword")
# u2 = User("Alice", "Johnson", "alice.johnson@example.com", "yetanotherpassword")
# u3 = User("Bob", "Brown", "bob.brown@example.com", "password123")
# session.add_all([u1, u2, u3])
# session.commit()

users = session.query(User).all()
for user in users:
    print(user) 

# t1 = Thing(1, "Laptop", "A personal computer for mobile use.", u1.id)
# t2 = Thing(2, "Smartphone", "A handheld personal computer.", u2.id)
# t3 = Thing(3, "Tablet", "A portable touch-screen computer.", u3.id)
# t4 = Thing(4, "Smartwatch", "A wearable computing device.", u1.id)
# session.add_all([t1, t2, t3, t4])
# session.commit()
things = session.query(Thing).all()
for thing in things:
    print(thing)
# session.close()

# Example of a parameterized query using SQLAlchemy's select
stmt = select(User).where(User.firstname == 'Jane')
result = session.execute(stmt)
for row in result.fetchall():
    print(row)