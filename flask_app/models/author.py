from ..config.mysqlconnection import connectToMySQL

from ..models import book

class Author:
    db = 'books_schema'
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.books=[]

    @classmethod
    def get_all(cls):
        query="SELECT * FROM authors;"
        results=connectToMySQL(cls.db).query_db(query)
        all_authors=[]
        for author in results:
            all_authors.append(cls(author))
        return all_authors

    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM authors "\
            "LEFT JOIN favorites ON authors.id=favorites.author_id "\
            "LEFT JOIN books ON favorites.book_id=books.id "\
            "WHERE authors.id=%(id)s;"
        results=connectToMySQL(cls.db).query_db(query, data)
        author=cls(results[0])
        if results[0]['books.id']!=None:
            for row in results:
                row_data={
                    'id':row['books.id'],
                    'title':row['title'],
                    'number_of_pages':row['number_of_pages'],
                    'created_at':row['books.created_at'],
                    'updated_at':row['books.updated_at']
                }
                author.books.append(book.Book(row_data))
        return author

    @classmethod
    def add_new(cls, data):
        query="INSERT INTO authors (name, created_at, updated_at) "\
            "VALUES (%(name)s, NOW(), NOW());"
        author_id=connectToMySQL(cls.db).query_db(query, data)
        return author_id

    @classmethod
    def add_favorite_book(cls, data):
        query="INSERT INTO favorites (author_id, book_id) "\
            "VALUES (%(author_id)s, %(book_id)s);"
        connectToMySQL(cls.db).query_db(query, data)
        
