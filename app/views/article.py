# app.py
from flask import Blueprint, render_template

from app.models import User
from app.repositories.article_repository import ArticleRepository

bp_articles = Blueprint("articles", __name__)

"""
articles = [
    {
        "titre": "Pourquoi apprendre Python aujourd'hui ?",
        "resume": "Python est devenu un langage incontournable pour le développement web, la data science et l'intelligence artificielle.",
        "auteur": "M. Ndiaye"
    },
    {
        "titre": "Introduction à l'Intelligence Artificielle",
        "resume": "Découvrez les principes fondamentaux de l'IA et les opportunités qu'elle offre aux étudiants en informatique.",
        "auteur": "Dr. Diop"
    },
    {
        "titre": "Hadoop et le Big Data : les bases",
        "resume": "Comprendre comment Hadoop permet de stocker et traiter des volumes massifs de données.",
        "auteur": "Laboratoire Data"
    }
]
"""

repo_articles = ArticleRepository()

def _initialiser_donnees():
    if repo_articles.lister():
        return

    from app.models import User
    from app.models import Article
    u1 = User("aminata@isi.sn", "Aminata", "Diallo")
    u2 = User("moussa@isi.sn", "Moussa", "Ndiaye")

    articles = [
        Article("Découvrir Flask", "Flask est un micro-framework web Flask est un micro-framework web…", u1),
        Article("Jinja2 en 5 minutes", "Jinja2 est le moteur de templates…", u1),
        Article("POO avec Python", "Les classes permettent de modéliser le métier…", u2),
    ]

    for article in articles:
        article.publier()
        repo_articles.enregistrer(article)






@bp_articles.route("/")
def article():
    return render_template("articles/article.html", articles=repo_articles.lister_publie())

@bp_articles.route("/<int:id>")
def detail(id):
    article = repo_articles.get(id)

    return render_template("articles/detail.html", article=article)

