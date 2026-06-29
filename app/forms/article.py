from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class ArticleForm(FlaskForm):
    titre = StringField(
        "Titre",
        validators=[
            DataRequired(message="Le titre est obligatoire"),
            Length(min=10,max=100, message="Entre 10 et 100 caractères")
        ]
    )

    contenu =TextAreaField(
        "Titre",
        validators=[
            DataRequired(message="Le titre est obligatoire"),
            Length(min=50, message="Au moins 50 caractères")
        ]
    )

    publier = BooleanField("Publier immédiatement")

    submit = SubmitField("Enregistrer")