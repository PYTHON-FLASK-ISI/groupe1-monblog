from flask import Flask

from app.extension import db, migrate, login_manager, csrf
from config import config_by_name


def create_app(nom_config="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(nom_config, config_by_name['dev']))
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    csrf.init_app(app)


    from app.cli import register_commands
    from .views.article import bp_articles
    from .views.produit import bp_produit
    from .views.main import bp_main
    from .views.admin import bp_admin
    from .views.auth import bp_auth



    app.register_blueprint(bp_articles)
    app.register_blueprint(bp_produit)
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_auth)
    register_commands(app)

#with app.app_context():
     #   from .views.article import _initialiser_donnees
    #    from .views.produit import _initialiser_donnees_produits
        #_initialiser_donnees()
        #_initialiser_donnees_produits()
        #db.create_all()
    return app
