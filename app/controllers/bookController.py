from flask import abort, flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app import app, db
from app.models import tables
from app.models.bookform import bookform



@app.route("/bookform", methods = ["GET", "POST"])
def addbook():
    form = bookform()
    if form.validate_on_submit():
        book = tables.Book(user_cpf= 1234, title=form.title.data, author=form.author.data, serie= form.serie.data, school= form.school.data, edition= form.edition.data, translateversion= form.translateversion.data, phisicalstate = form.phisicalstate.data, price = form.price.data, type= form.type.data)
        print(form.title.data)
        print(form.price.data)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Voce adicionou um livro com sucesso!')
        except:
            flash('Erro ao adicionar livro')

    return render_template('bookform.html',  title="Balaio de Livros", form = form)

@app.route("/bookform/editbook/<id>",  methods = ["GET", "POST"])
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

@app.route("/bookform",  methods = ["GET", "POST"])
def upload(request):
    file = request.files['inputFile']
    newFile = tables.BookImage(name=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()
    flash(file.filename + "salvo com sucesso!")