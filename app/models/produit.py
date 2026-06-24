from app.models.base import BaseModel
from app import db

class Produit(BaseModel):

    __tablename__ = "produits"
    __table_args__ = {'schema': 'blog'}
    """
    def __init__(self  , nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    """
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    proprietaire_id = db.Column(db.Integer, db.ForeignKey('blog.users.id'), nullable=False)
    proprietaire = db.relationship('User', backref='blog.produits')

    def vendre(self, quantite):
        if (quantite > self.stock):
            raise ValueError("Stock insuffisant")
        self.stock -= quantite