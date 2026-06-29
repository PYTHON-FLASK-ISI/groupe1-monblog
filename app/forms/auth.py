from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class InscriptionForm(FlaskForm):

    email=StringField("Email", validators=[DataRequired(),Email()])
    prenom = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=50)])
    nom = StringField("Nom", validators=[DataRequired(), Length(min=2, max=50)])
    mdp = PasswordField("Mot de passe",
                        validators=[DataRequired(),
                                    Length(min=8, message=("8 caractères minimum"))])

    mdp_confirm = PasswordField("Confirmation du mot de passe",
                                validators=[DataRequired(),

                                            EqualTo("mdp", message="Les mots de passe ne correspondent pas")
                                            ])
    submit = SubmitField("Créer mon compte")

    def valider_email(self, field):
        from ..models import User
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Cet email est déjà utilisé")


class ConnexionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    se_souvenir = BooleanField("Se souvenir de moi")
    submit = SubmitField("Se connecter")