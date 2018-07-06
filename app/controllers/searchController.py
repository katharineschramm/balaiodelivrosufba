from flask import flash, render_template, redirect, url_for, request
import flask_whooshalchemy as whooshalchemy
from app import app, db
from app.models import tables
from app.models.searchModel import searchModel
from config import MAX_SEARCH_RESULTS

@app.route('/', methods=['GET','POST'])
@app.route('/search', methods=['GET','POST'])
def search():
    form= searchModel(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('searchresults', search= form.search.data))


@app.route('/searchresults/<search>')
def searchresults(search):
    results = tables.Book.query.whoosh_search(search, MAX_SEARCH_RESULTS).all()
    return render_template('searchresults.html', title="Balaio de Livros", search=search, results=results)
