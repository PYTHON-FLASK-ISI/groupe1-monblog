from app import db
from datetime import datetime, timezone


class BaseModel(db.Model):

    __abstract__ = True # Cette classe sert d'héritage pour les autres classes, ne pas créer la table

    id = db.Column(db.Integer, primary_key=True)
    cree_le = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    maj_le = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def maj(self):
        self.maj_le = datetime.now(timezone.utc)



    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"