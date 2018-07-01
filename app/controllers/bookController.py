from flask import abort, flash, redirect, url_for, render_template
from app import app, db
from app.models import tables
from app.models.bookform import bookform
from . import book


@app.route("/bookform", methods = ["GET", "POST"])
def addbook():
    form = bookform()
    if form.validate_on_submit():
        book = tables.Book(title=form.title.data, author=form.author.data, serie= form.serie.data, school= form.school.data, edition= form.edition.data, translateversion= form.translateversion.data, phisicalstate = form.phisicalstate.data, price = form.price.data)
        print(form.title.data)
        print(form.price.data)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Voce adicionou um livro com sucesso!')
        except:
            flash('Erro ao adicionar livro')
            #return render_template('bookform.html', title="Balaio de Livros", form = form)
    return render_template('bookform.html',  title="Balaio de Livros", form = form)

@book.route("/bookform/editbook/<id>",  methods = ["GET", "POST"])
def editbook(id):
    book = tables.Book.query.filter_by(id= id).limit(1)
    return render_template("/bookform/editbook/<id>", book=book)

@app.route("/listbooks",  methods = ["GET", "POST"])
def listbooks():
   # con = db.connect("balaio.db")
    books = tables.Book.query.all()
    return render_template("listbooks.html", books=books)

@app.route("/listbooks/deletebook/<id>",  methods = ["GET", "POST"])
def deletebook(id):
    book = tables.Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')