from flask import Flask
from app.extension import db,migrate



def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Passer123@localhost:5432/blog_app_groupe1'
    db.init_app(app)
    migrate.init_app(app,db)

    from app.cli import register_commands
    from .views.article import bp_articles
    from .views.produit import bp_produit
    app.register_blueprint(bp_articles)
    app.register_blueprint(bp_produit)
    register_commands(app)

    with app.app_context():
        from .views.article import _initialiser_donnees
        from .views.produit import _initialiser_donnees_produits
        #_initialiser_donnees()
        #_initialiser_donnees_produits()
        #db.create_all()
    return app