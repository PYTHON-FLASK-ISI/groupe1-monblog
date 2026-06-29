from flask import Blueprint, render_template
from sqlalchemy import func

from app import db
from app.models import User, Article

bp_main = Blueprint('main', __name__)
@bp_main.route('/')
def accueil():
    top_auteurs = (
        db.session.query(User, func.count(Article.id).label('nb_articles'))
        .join(Article, Article.auteur_id == User.id)
        .filter(Article.publie.is_(True))
        .group_by(User.id)
        .order_by(func.count(Article.id).desc())
        .limit(5)
        .all()
    )
    derniers_articles = (Article.query.filter_by(publie=True)
                         .order_by(Article.cree_le.desc())
                         .limit(3)
                         .all())
    return render_template(
        "main/accueil.html", top_auteurs=top_auteurs, derniers_articles=derniers_articles
    )