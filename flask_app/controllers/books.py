from flask_app import app

from flask import render_template, redirect, request

from ..models.book import Book
from ..models import author

@app.route('/books')
def all_books():
    all_books=Book.get_all()
    return render_template('books.html', all_books=all_books)

@app.route('/books/<int:id>')
def show_one_book(id):
    current_book=Book.get_one({'id':id})
    all_authors=author.Author.get_all()
    return render_template('show_book.html', book=current_book, all_authors=all_authors)

@app.route('/books/<int:id>/favorite', methods=['POST'])
def add_favorite_author(id):
    data={
        'book_id':id,
        'author_id':request.form['author_id']
    }
    Book.add_favorite_author(data)
    return redirect(f"/books/{id}")

@app.route('/books/create', methods=['POST'])
def add_book():
    Book.add_new(request.form)
    return redirect('/books')