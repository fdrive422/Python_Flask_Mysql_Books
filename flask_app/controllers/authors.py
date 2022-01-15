from flask_app import app
from flask import render_template, redirect, request

from ..models.author import Author
from ..models import book

# root route show all authors
@app.route('/')
def home():
    return redirect('/authors')

# show all authors
@app.route('/authors')
def all_authors():
    all_authors=Author.get_all()
    return render_template('authors.html', all_authors=all_authors)

@app.route('/authors/<int:id>')
def show_one_author(id):
    current_author=Author.get_one({'id':id})
    all_books=book.Book.get_all()
    return render_template('show_author.html', author=current_author, all_books=all_books)

@app.route('/authors/<int:id>/favorite', methods=['POST'])
def add_favorite_book(id):
    data={
        'author_id':id,
        'book_id':request.form['book_id']
    }
    Author.add_favorite_book(data)
    return redirect(f"/authors/{id}")

@app.route('/authors/create', methods=['POST'])
def add_author():
    Author.add_new(request.form)
    return redirect('/authors')