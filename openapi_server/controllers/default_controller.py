from uuid import uuid4
import connexion
from typing import Dict
from typing import Tuple
from typing import Union

import connexion.cli
import connexion.lifecycle
import connexion.mock
import connexion.options
import connexion.security
from flask import make_response
import openapi_server.db as db

import connexion.resources
import connexion.resources.schemas
from openapi_server.models.author import Author  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.create_book_request import CreateBookRequest  # noqa: E501
from openapi_server.models.create_user_request import CreateUserRequest  # noqa: E501
from openapi_server.models.genre import Genre  # noqa: E501
from openapi_server.models.get_users_books200_response_inner import GetUsersBooks200ResponseInner  # noqa: E501
from openapi_server.models.post_authors_request import PostAuthorsRequest  # noqa: E501
from openapi_server.models.set_user_read_pages_request import SetUserReadPagesRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def create_book(create_book_request=None):  # noqa: E501
    """Create a book

     # noqa: E501

    :param create_book_request: 
    :type create_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """

    if connexion.request.is_json:
        create_book_request = CreateBookRequest.from_dict(
            connexion.request.get_json())
    new_book = Book(id=str(uuid4()), title=create_book_request.title,
                    author=findAuthor(create_book_request.author),
                    number_of_pages=create_book_request.number_of_pages,
                    genres=[findGenre(genreId) for genreId in create_book_request.genres])
    
    db.books.append(new_book)
    # noqa: E501
    return new_book, 201


def create_genre(body=None):  # noqa: E501
    """add new genre

     # noqa: E501

    :param body: 
    :type body: str

    :rtype: Union[Genre, Tuple[Genre, int], Tuple[Genre, int, Dict[str, str]]
    """
    new_genre = Genre(str(uuid4()), body)
    db.genres.append(new_genre)
    return new_genre, 201


def create_user(create_user_request=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param create_user_request: 
    :type create_user_request: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_user_request = CreateUserRequest.from_dict(
            connexion.request.get_json())

      # noqa: E501

    new_user = User(str(uuid4()), create_user_request.first_name,
                    create_user_request.last_name)
    db.users.append(new_user)
    return new_user, 201


def get_authors():  # noqa: E501
    """List authors

     # noqa: E501


    :rtype: Union[List[Author], Tuple[List[Author], int], Tuple[List[Author], int, Dict[str, str]]
    """
    return db.authors


def get_authors_author_id(author_id):  # noqa: E501
    """get author by id

     # noqa: E501

    :param author_id: 
    :type author_id: str

    :rtype: Union[Author, Tuple[Author, int], Tuple[Author, int, Dict[str, str]]
    """
    author = next((x for x in db.authors if x.id == author_id), None)
    if author is not None:
        response = make_response(author)
        response.status_code = 200
        return response
    else:
        return connexion.problem(404, 'Author not found', 'Author not found')


def get_book_by_id(book_id):  # noqa: E501
    """Book by id

     # noqa: E501

    :param book_id: 
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    book = next((x for x in db.books if x.id == book_id), None)
    if book is not None:
        response = make_response(book)
        response.status_code = 200
        return response
    else:
        return connexion.problem(404, 'Book not found', 'Book not found')


def get_books(author=None, genres=None):  # noqa: E501
    """List books

     # noqa: E501

    :param author: 
    :type author: str
    :param genres: 
    :type genres: List[str]

    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """

    print('getting books')

    def checkAuthor(b: Book):
        if author is None:
            return True
        else:
            return b.author.id == author

    def checkGenres(b: Book):
        if genres is None:
            return True
        else:
            return b.author.id in genres

    books = [book for book in db.books if checkAuthor(
        book) and checkGenres(book)]

    return books


def get_genres():  # noqa: E501
    """List genres

     # noqa: E501


    :rtype: Union[List[Genre], Tuple[List[Genre], int], Tuple[List[Genre], int, Dict[str, str]]
    """
    return db.genres


def get_user_by_id(user_id):  # noqa: E501
    """get user by userid

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """

    user = next((user for user in db.users if user.id == user_id), None)

    if user is None:
        return connexion.problem(404, 'User not found', 'User not found')
    else:
        return user


def findBook(bookId) -> Book: return next((
        book for book in db.books if book.id == bookId), None)

def findGenre(genreId) -> Genre: return next((
        genre for genre in db.genres if genre.id == genreId), None)

def findAuthor(authorId) -> Author: return next((
        author for author in db.authors if author.id == authorId), None)


def get_users_books(user_id):  # noqa: E501
    """user&#39;s books

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str

    :rtype: Union[List[GetUsersBooks200ResponseInner], Tuple[List[GetUsersBooks200ResponseInner], int], Tuple[List[GetUsersBooks200ResponseInner], int, Dict[str, str]]
    """

    

    userbooks = [   GetUsersBooks200ResponseInner(findBook(bookId), pagesRead)
                     for (user, bookId, pagesRead) in db.userBooks
                     if user == user_id]
    
    return userbooks


def post_authors(post_authors_request=None):  # noqa: E501
    """Add author

     # noqa: E501

    :param post_authors_request: 
    :type post_authors_request: dict | bytes

    :rtype: Union[Author, Tuple[Author, int], Tuple[Author, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_authors_request = PostAuthorsRequest.from_dict(
            connexion.request.get_json())

    author = Author(str(uuid4()), post_authors_request.first_name, post_authors_request.last_name)  # noqa: E501
    db.authors.append(author)

    return author, 201


def set_user_read_pages(user_id, set_user_read_pages_request=None):  # noqa: E501
    """Set read pages for a book

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str
    :param set_user_read_pages_request: 
    :type set_user_read_pages_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        set_user_read_pages_request = SetUserReadPagesRequest.from_dict(connexion.request.get_json())  # noqa: E501

    newList = [(userId, bookId, pages) for (userId, bookId, pages) in db.userBooks if userId !=
               user_id and bookId != set_user_read_pages_request.book_id]
    
    
    newList.append((user_id, set_user_read_pages_request.book_id,
                   set_user_read_pages_request.pages_read))

    db.userBooks = newList

    return None, 200
