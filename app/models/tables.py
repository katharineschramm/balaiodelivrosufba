from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"

    cpfuser = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pw_hash = db.Column(db.String(80))
    address = db.Column(db.Text, nullable=False)
    reputation = db.Column(db.Float)
    dtbirth = db.Column(db.Date)
    grant = db.Column(db.Integer)

    def __init__(self, cpfuser, name, email, address, reputation, dtbirth, grant):
        self.name = name
        self.cpfuser = cpfuser
        self.email = email
        self.address = address
        self.reputation = reputation
        self.dtbirth = dtbirth
        self.grant = grant

    @property
    def password(self):
        """
        Impede que a senha seja acessada
        """
        raise AttributeError('A senha e um atributo secreto.')

    @password.setter
    def password(self, password):
        """
        Faz o hash da senha
        """
        self.pw_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        """
        verifica se o hash corresponde a senha
        """
        return check_password_hash(self.pw_hash, password)
    
    def __repr__(self):
        return "<User %r>" % self.name
     
class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    serie = db.Column(db.String(80), nullable=False)
    school = db.Column(db.String(80), nullable=False)
    edition =   db.Column(db.String(80), nullable=False)
    translateversion = db.Column(db.String(80))
    phisicalstate = db.Column(db.Text, nullable=False)
    sold = db.Column(db.Integer)
    price = db.Column(db.Float)
    user_cpf = db.Column(db.Integer, db.ForeignKey("users.cpfuser"))
    
    user = db.relationship('User', foreign_keys = user_cpf)

    def __init__ (self, title, author, serie, school, edition, translateversion, phisicalstate, sold, price, user_cpf):
        self.title = title
        self.author = author
        self.serie = serie
        self.school = school
        self.edition = edition
        self.translateversion = translateversion
        self.phisicalstate = phisicalstate
        self.sold = sold
        self.price = price
        self.user_cpf= user_cpf

    def __repr__(self):
        return "<Book %r>" % self.title     

class Interest(db.Model):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_cpf = db.Column(db.Integer, db.ForeignKey("users.cpfuser"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    user = db.relationship('User', foreign_keys = user_cpf)
    book = db.relationship('Book', foreign_keys = book_id)

    def __init__ (self, user_cpf, book_id):
        self.user_cpf = user_cpf
        self.book_id = book_id
    
    def __repr__(self):
        return "<Interest %r>"% self.book_id
    
class Ad(db.Model):
    __tablename__ = "ads"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_cpf = db.Column(db.Integer, db.ForeignKey("users.cpfuser"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    user = db.relationship('User', foreign_keys = user_cpf)
    book = db.relationship('Book', foreign_keys = book_id)

    def __init__ (self, user_cpf, book_id):
        self.user_cpf = user_cpf
        self.book_id = book_id
    
    def __repr__(self):
        return "<Interest %r>"% self.book_id