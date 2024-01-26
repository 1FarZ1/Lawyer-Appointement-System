




from app.config.database import SessionLocal
from app.models import Categorie


def get_lawyer_categories(db:SessionLocal):
    return db.query(Categorie).all()
