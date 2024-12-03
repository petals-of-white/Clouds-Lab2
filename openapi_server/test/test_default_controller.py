import unittest

from flask import json

from openapi_server.models.author import Author  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.create_book_request import CreateBookRequest  # noqa: E501
from openapi_server.models.create_user_request import CreateUserRequest  # noqa: E501
from openapi_server.models.genre import Genre  # noqa: E501
from openapi_server.models.get_users_books200_response_inner import GetUsersBooks200ResponseInner  # noqa: E501
from openapi_server.models.post_authors_request import PostAuthorsRequest  # noqa: E501
from openapi_server.models.set_user_read_pages_request import SetUserReadPagesRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        Create a book
        """
        create_book_request = openapi_server.CreateBookRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/books',
            method='POST',
            headers=headers,
            data=json.dumps(create_book_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_genre(self):
        """Test case for create_genre

        add new genre
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/genres',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        create_user_request = openapi_server.CreateUserRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/users',
            method='POST',
            headers=headers,
            data=json.dumps(create_user_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_authors(self):
        """Test case for get_authors

        List authors
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/authors',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_authors_author_id(self):
        """Test case for get_authors_author_id

        get author by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/authors/{author_id}'.format(author_id='author_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        Book by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/books/{book_id}'.format(book_id='book_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_books(self):
        """Test case for get_books

        List books
        """
        query_string = [('author', 'author_example'),
                        ('genres', ['genres_example'])]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/books',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genres(self):
        """Test case for get_genres

        List genres
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/genres',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        get user by userid
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/users/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_books(self):
        """Test case for get_users_books

        user's books
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/users/{user_id}/books'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_authors(self):
        """Test case for post_authors

        Add author
        """
        post_authors_request = openapi_server.PostAuthorsRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/authors',
            method='POST',
            headers=headers,
            data=json.dumps(post_authors_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_user_read_pages(self):
        """Test case for set_user_read_pages

        Set read pages for a book
        """
        set_user_read_pages_request = openapi_server.SetUserReadPagesRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MAKSYMSYVASH_1/BooksManager/1.0.0/users/{user_id}/books'.format(user_id='user_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(set_user_read_pages_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
