# app.py

from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required

from app import db
from app.forms.article import ArticleForm
from app.models import User, Article
from app.repositories.article_repository import ArticleRepository

bp_articles = Blueprint("articles", __name__,url_prefix="/articles")



def _filtrer_requete():
    q = Article.query.filter_by(publie=True)
    mot = request.args.get('mot')
    if mot:
        q = q.filter(
            Article.titre.ilike(f'%{mot}%') | Article.contenu.ilike(f'%{mot}%')
        )
        
    auteur = request.args.get('auteur')
    if auteur:
        q = q.join(Article.auteur).filter(User.email.ilike(f'%{auteur}%'))
    return q.order_by(Article.cree_le.desc())


@bp_articles.route("/")
def article():
    page = request.args.get('page', 1, type=int)
    pagination = _filtrer_requete().paginate(page=page, per_page=5, error_out=False)
    return render_template(
        "articles/article.html",
        articles=pagination.items,
        pagination=pagination,
        q=request.args.get('mot',''),
        auteur=request.args.get('auteur','')
                           )

@bp_articles.route("/<int:id>", methods=['GET', 'POST'])
def detail(id):
    article = db.session.get(Article, id)

    return render_template("articles/detail.html", article=article)

@bp_articles.route("/nouveau", methods=['GET', 'POST'])
@login_required
def creer():
    form = ArticleForm()
    utilisateurs = User.query.order_by(User.nom).all()
    if form.validate_on_submit():
        auteur_id = request.form.get('auteur_id', type=int) or (
            utilisateurs[0].id if utilisateurs else 1
        )

        article = Article (
            titre=form.titre.data,
            contenu=form.contenu.data,
            auteur_id=auteur_id,
            publie=form.publier.data
        )
        db.session.add(article)
        db.session.commit()
        return redirect((url_for('articles.detail', id=article.id)))
    return render_template(
        'articles/formulaire.html',
        form=form,
        utilisateurs=utilisateurs,
        article = None
    )

@bp_articles.route("/<int:id>/modifier", methods=['GET', 'POST'])
@login_required
def modifier(id):
    article = db.session.get(Article, id)
    utilisateurs = User.query.order_by(User.nom).all()
    if article is None:
        abort(404)

    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        article.titre = form.titre.data
        article.contenu = form.contenu.data
        article.publie = form.publier.data
        db.session.commit()
        return redirect((url_for('articles.detail', id=article.id)))
    return render_template(
        'articles/formulaire.html',
        form=form,
        utilisateurs=utilisateurs,
        article = article
    )



@bp_articles.route("/<int:id>/supprimer", methods=['POST'])
@login_required
def supprimer(id):
    article = db.session.get(Article, id)
    if article is None:
        abort(404)

    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('articles.article'))