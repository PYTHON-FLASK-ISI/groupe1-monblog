from app.models.base import BaseModel
from app import db


class Article(BaseModel):

    __tablename__ = "articles"
    __table_args__ = {'schema': 'blog'}

    """
    def __init__(self, titre, resume, auteur):
        super().__init__()
        self.titre = titre
        self.contenu = resume
        self.auteur = auteur
        self.publie = False
        self.commentaires = []

    """
    titre = db.Column(db.String(100), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    publie = db.Column(db.Boolean, default=False)
    auteur_id = db.Column(db.Integer, db.ForeignKey('blog.users.id'), nullable=False)
    auteur = db.relationship('User', back_populates='articles')
    commentaires = db.relationship('Commentaire', backref='articles',cascade="all, delete-orphan", lazy='dynamic')

    def publier(self):
        if not self.titre:
            raise ValueError("Le titre est obligatoire")
        self.publie = True
        self.maj()

    def resume(self, longueur=120):
        if len(self.contenu) > longueur:
            return self.contenu[:longueur] + "..."
        return self.contenu

    def valider(self):
        if not self.titre:
            raise ValueError("Le titre est obligatoire")
        if not self.contenu:
            raise ValueError("Le contenu est obligatoire")
        if not self.auteur:
            raise ValueError("L'auteur est obligatoire")

    def ajouter_commentaire(self, commentaire):
        commentaire.article = self
        self.commentaires.append(commentaire)
