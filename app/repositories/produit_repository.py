from app.models.produit import Produit
from app.repositories.base_repository import BaseRepository


class ProduitRepository(BaseRepository[Produit]):
    def produits_disponible(self)-> list[Produit]:
        return [p for p in self.lister() if p.stock > 0]

    def rechercher_par_nom(self, nom:str)-> list[Produit]:
        return [p for p in self.lister() if nom.lower() in p.nom.lower()]