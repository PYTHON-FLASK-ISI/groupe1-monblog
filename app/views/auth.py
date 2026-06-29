from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user

from app import db
from app.forms.auth import InscriptionForm, ConnexionForm
from app.models import User

bp_auth = Blueprint('auth', __name__,url_prefix="/auth")

@bp_auth.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if current_user.is_authenticated:
        return redirect(url_for('articles.article'))

    form = InscriptionForm()
    if form.validate_on_submit():
        user = User(
            email= form.email.data.lower(),
            prenom=form.prenom.data,
            nom=form.nom.data

        )
        print(user)
        user.definir_mdp(form.mdp.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.connexion'))
    return render_template(
        "auth/inscription.html",
        form=form
    )

@bp_auth.route("/connexion", methods=['GET', 'POST'])
def connexion():
    if current_user.is_authenticated:
        return redirect(url_for('articles.article'))
    form = ConnexionForm()
    if form.validate_on_submit():
        #print('POST')
        user = User.query.filter_by(email=form.email.data.lower()).first()
        #print(user, user.verifier_mdp(form.mdp.data))
        if user and user.verifier_mdp(form.mdp.data):
            #print('OK',user)
            login_user(user, remember=form.se_souvenir.data)
            next_url = request.args.get('next') or url_for('articles.article')
            if next_url.startswith('/'):
                return redirect(next_url)
            return redirect(url_for('main.accueil'))

    return render_template("auth/connexion.html", form=form)


@bp_auth.route("/deconnexion")
@login_required
def deconnexion():
    logout_user()
    return redirect(url_for('main.accueil'))