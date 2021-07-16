from db_session import db_session, engine
from base import Base

def init_db():

    from models.products import Products
    
    Base.metadata.create_all(bind=engine)

    db_session.commit()