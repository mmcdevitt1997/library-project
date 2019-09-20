from django.conf.urls import url
from .views import *
from django.conf.urls import url, include

app_name = "libraryapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$',librarian_list, name='librarians'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^books$', book_list, name='books'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^libraries$', library_list, name='libraries'),
]