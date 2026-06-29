from app.models.base import BaseModel
from app import db

class Commentaire(BaseModel):

    __tablename__ = "commentaires"

    __table_args__ = {'schema': 'blog'}
    """
    def __init__(self,contenu, auteur):
        super().__init__()
        self.contenu = contenu
        self.auteur = auteur
        self.article = None
    """
    contenu = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('blog.articles.id'), nullable=False)
    auteur_id = db.Column(db.Integer, db.ForeignKey('blog.users.id'), nullable=False)

    auteur = db.relationship('User')
    #article = db.relationship('Article', back_populates='commentaires')

    def valider(self):
        if not self.contenu or not self.contenu.strip():
            raise ValueError("Le contenu du commentaire est obligatoire")
        if not self.auteur:
            raise ValueError("L'auteur est obligatoire")