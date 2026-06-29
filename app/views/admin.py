from flask import Blueprint, render_template
from flask_login import login_required

from app.decorator import admin_required
from app.models import User

bp_admin = Blueprint('admin', __name__,url_prefix="/admin")

@bp_admin.route('/utilisateurs')
@login_required
@admin_required
def utilisateurs():
    users = User.query.order_by(User.cree_le).all()
    return render_template(
        "admin/utilisateurs.html",users=users
    )