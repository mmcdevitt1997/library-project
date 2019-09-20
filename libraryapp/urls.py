from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.urls import path

app_name = "libraryapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$', book_list, name='home'),
     url(r'^library$', library_list, name='library'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$',librarian_list, name='librarians'),
    url(r'^book/form$', book_form, name='book_form'),

    url(r'^library/form$', library_form, name='library_form'),
    url(r'^libraries$', library_list, name='libraries'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    path('library/<int:library_id>/', library_details, name='library'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
]