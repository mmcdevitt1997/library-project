import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection



def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn_number,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                book = Book()
                book.id = row['id']
                book.title = row['title']
                book.isbn_number = row['isbn_number']
                book.author = row['author']
                book.year_published = row['year_published']
                book.librarian_id = row['librarian_id']
                book.location_id = row['location_id']

                all_books.append(book)

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn_number,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['author'],
                form_data['isbn_number'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))
