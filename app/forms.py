from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField

class RecipeForm(FlaskForm):
    title = StringField('title', validators=[validators.DataRequired()])
    description = TextAreaField('description', validators=[validators.Length(min=1, max=255)]) # description text field with min 1 character max 255
    ingredients = TextAreaField('ingredients', validators=[validators.Length(min=1, max=255)]) # text field with same validators
    instructions = TextAreaField('instructions', validators=[validators.Length(min=1, max=255)]) # text field with same validators
    submit = SubmitField("Submit Recipe") # submit field 



class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit =  SubmitField("Sign in")
    remember_me = BooleanField("Remember Me")
