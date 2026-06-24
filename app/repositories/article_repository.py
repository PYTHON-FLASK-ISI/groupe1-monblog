from app.models import Article
from app.repositories.base_repository import BaseRepository


class ArticleRepository(BaseRepository[Article]):
    def lister_publie(self)-> list[Article]:
        return [a for a in self.lister() if a.publie]

    def chercher_par_auteur(self,email:str)-> list[Article]:
        return [ a for a in self.lister() if a.auteur.email == email]

    def chercher_par_mot_cle(self,mot:str)-> list[Article]:
        mot = mot.lower()
        return [a for a in self.lister() if mot in a.titre.lower() or mot in a.contenu.lower()]