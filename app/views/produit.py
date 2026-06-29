from flask import Blueprint, render_template

from app.models.produit import Produit
from app.repositories.produit_repository import ProduitRepository

bp_produit = Blueprint("produits", __name__)


repo_produits = ProduitRepository()

def _initialiser_donnees_produits():
    if repo_produits.lister():
        return
    from app.models.produit import Produit
    produitss = [
        Produit("Ordinateur Portable", 450000, 10),
        Produit("Souris Sans Fil", 15000, 25),
        Produit("Machine à laver", 15000, 25),
    ]

    for p in produitss:
        repo_produits.enregistrer(p)


@bp_produit.route("/produits")
def produits():
    return render_template("produits/produit.html", produits=Produit.query.all())

