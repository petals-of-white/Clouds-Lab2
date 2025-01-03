from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.author import Author
from openapi_server.models.genre import Genre
from openapi_server import util

from openapi_server.models.author import Author  # noqa: E501
from openapi_server.models.genre import Genre  # noqa: E501

class Book(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, title=None, number_of_pages=None, genres=None, author=None):  # noqa: E501
        """Book - a model defined in OpenAPI

        :param id: The id of this Book.  # noqa: E501
        :type id: str
        :param title: The title of this Book.  # noqa: E501
        :type title: str
        :param number_of_pages: The number_of_pages of this Book.  # noqa: E501
        :type number_of_pages: int
        :param genres: The genres of this Book.  # noqa: E501
        :type genres: List[Genre]
        :param author: The author of this Book.  # noqa: E501
        :type author: Author
        """
        self.openapi_types = {
            'id': str,
            'title': str,
            'number_of_pages': int,
            'genres': List[Genre],
            'author': Author
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'number_of_pages': 'numberOfPages',
            'genres': 'genres',
            'author': 'author'
        }

        self._id = id
        self._title = title
        self._number_of_pages = number_of_pages
        self._genres = genres
        self._author = author

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Book.


        :return: The id of this Book.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Book.


        :param id: The id of this Book.
        :type id: str
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Book.


        :return: The title of this Book.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Book.


        :param title: The title of this Book.
        :type title: str
        """

        self._title = title

    @property
    def number_of_pages(self) -> int:
        """Gets the number_of_pages of this Book.


        :return: The number_of_pages of this Book.
        :rtype: int
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        """Sets the number_of_pages of this Book.


        :param number_of_pages: The number_of_pages of this Book.
        :type number_of_pages: int
        """

        self._number_of_pages = number_of_pages

    @property
    def genres(self) -> List[Genre]:
        """Gets the genres of this Book.


        :return: The genres of this Book.
        :rtype: List[Genre]
        """
        return self._genres

    @genres.setter
    def genres(self, genres: List[Genre]):
        """Sets the genres of this Book.


        :param genres: The genres of this Book.
        :type genres: List[Genre]
        """

        self._genres = genres

    @property
    def author(self) -> Author:
        """Gets the author of this Book.


        :return: The author of this Book.
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author: Author):
        """Sets the author of this Book.


        :param author: The author of this Book.
        :type author: Author
        """

        self._author = author
