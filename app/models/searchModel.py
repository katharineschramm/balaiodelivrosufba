from flask_wtf import FlaskForm
from wtforms.fields.html5 import SearchField
from wtforms.validators import DataRequired

class searchModel(FlaskForm):
    search = SearchField("search", validators= [DataRequired()])

