from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import BaseModel
from app import db, login_manager


class User(UserMixin,BaseModel):

    __tablename__ = "users"
    __table_args__ = {'schema': 'blog'}
    """
    def __init__(self, email:str, prenom:str, nom:str):
        super().__init__()
        self.email = email
        self.prenom = prenom
        self.nom = nom
        self._mdp_hash = None
    """
    email = db.Column(db.String(100), unique=True, nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    _mdp_hash = db.Column('mdp_hash', db.Text, nullable=False)
    actif = db.Column(db.Boolean, default=False)
    role= db.Column(db.String(50), default="utilisateur")
    articles = db.relationship('Article', back_populates='auteur', cascade="all, delete-orphan", lazy='dynamic')


    def definir_mdp(self, mdp_clair:str) -> None:
        self._mdp_hash = generate_password_hash(mdp_clair)

    def verifier_mdp(self, mdp_clair:str) -> bool:
        if not self._mdp_hash :
            return False
        return check_password_hash(self._mdp_hash, mdp_clair)

    def valider(self):
        if '@' not in self.email:
            raise ValueError("L'email est invalide")
        if not self.prenom or self.nom:
            raise ValueError("Prénom et nom obligatoires")

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}".strip()

    @property
    def est_admin(self)->bool:
        return self.role == "admin"

    @property
    def est_auteur(self):
        return self.role in ('auteur','admin')

    def __repr__(self):
        return f"<User {self.nom_complet}>"

@login_manager.user_loader
def charger_user(id):
    return db.session.get(User, int(id))