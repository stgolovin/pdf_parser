import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Years(Base):
    __tablename__ = 'data'

    id = sq.Column(sq.Integer, primary_key=True)
    text = sq.Column(sq.Text)

def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
