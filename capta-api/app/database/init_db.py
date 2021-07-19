from .db_session import db_session, engine
from .base import Base

def init_db():

    from products.models import ProductsModel
    
    Base.metadata.create_all(bind=engine)

    db_session.commit()