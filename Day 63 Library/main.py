from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False) 

    def __repr__(self):
        return '<Books %r>' % self.title

#### this is for the sqlite3 ####

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# app = Flask(__name__)

all_books = []

##################################

# create an entry
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating="9.3")
# db.session.add(book)
# db.session.commit()

@app.route('/')
def home():
    # read all books
    all_books = db.session.query(Books).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # new_book = {
        #     "title": request.form["title"],
        #     "author": request.form["author"],
        #     "rating": request.form["rating"]
        # }
        # all_books.append(new_book)
        # print(all_books)

        new_book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        book_id = id
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form['newrating']
        db.session.commit() 
        return redirect(url_for('home'))
    book = Books.query.filter_by(id=id).first()
    return render_template("edit.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)

