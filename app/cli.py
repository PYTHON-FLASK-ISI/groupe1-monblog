import click
from flask.cli import with_appcontext

from app import db
from app.models import User, Article, Produit

@click.command("seed")
@with_appcontext
def seed():
    if User.query.first():
        click.echo("La base contient des données")
        return

    users=[
        User(email="aminata@isi.sn", prenom="Aminata", nom="Diallo"),
        User(email="moussa@isi.sn", prenom="Moussa", nom="Ndiaye"),
        User(email="fatou@isi.sn", prenom="Fatou", nom="Sarr")
    ]
    for u in users:
        u.definir_mdp("Password123")
        db.session.add(u)
    db.session.flush()

    articles_data = [
        ("Découvrir Flask", "Flask est un micro-framework web idéal pour apprendre.", users[0], True),
        ("Jinja2 en pratique", "Les templates Jinja2 séparent HTML et logique.", users[0], True),
        ("Routes dynamiques", "Les convertisseurs int et float valident les URL.", users[1], True),
        ("PostgreSQL et Flask", "SQLAlchemy relie les modèles Python à PostgreSQL.", users[1], True),
        ("Migrations Alembic", "Flask-Migrate versionne le schéma de la base.", users[1], False),
        ("CRUD complet", "Create, Read, Update, Delete sur les articles.", users[2], True),
        ("Pagination", "Afficher de longues listes page par page.", users[2], True),
        ("Les Blueprints", "Structurer une application en modules.", users[0], True),
        ("Sessions utilisateur", "Gérer l'état connecté avec Flask-Login.", users[2], False),
        ("Sécurité web", "CSRF, hash des mots de passe, validation serveur.", users[1], True),
    ]

    for titre, contenu, auteur, publie in articles_data:
        art=Article(titre=titre, contenu=contenu, auteur_id=auteur.id,publie=publie)
        db.session.add(art)
    db.session.flush()

    produits_data = [
        ('Ordinateur Portable', 450000, 10, users[0]),
        ('Souris Sans Fil', 15000, 25, users[1]),
        ('Clavier Mécanique', 35000, 12, users[2])
    ]

    for nom, prix, stock, proprietaire in produits_data:
        produit = Produit(nom=nom, prix=prix, stock=stock, proprietaire_id=proprietaire.id)
        db.session.add(produit)
    db.session.flush()

    db.session.commit()
    click.echo("Insertion des données terminée")

def register_commands(app):
    app.cli.add_command(seed)