from app import app
from flask import render_template, redirect, request

from app.models.searchModel import searchModel
#from app.models.forms import LoginForm


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print (form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = searchModel()
    return render_template("index.html", title = "Balaio de Livros", form=form)