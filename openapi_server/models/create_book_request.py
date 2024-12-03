from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateBookRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, author=None, genres=None, number_of_pages=None):  # noqa: E501
        """CreateBookRequest - a model defined in OpenAPI

        :param title: The title of this CreateBookRequest.  # noqa: E501
        :type title: str
        :param author: The author of this CreateBookRequest.  # noqa: E501
        :type author: str
        :param genres: The genres of this CreateBookRequest.  # noqa: E501
        :type genres: List[str]
        :param number_of_pages: The number_of_pages of this CreateBookRequest.  # noqa: E501
        :type number_of_pages: int
        """
        self.openapi_types = {
            'title': str,
            'author': str,
            'genres': List[str],
            'number_of_pages': int
        }

        self.attribute_map = {
            'title': 'title',
            'author': 'author',
            'genres': 'genres',
            'number_of_pages': 'numberOfPages'
        }

        self._title = title
        self._author = author
        self._genres = genres
        self._number_of_pages = number_of_pages

    @classmethod
    def from_dict(cls, dikt) -> 'CreateBookRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The create_book_request of this CreateBookRequest.  # noqa: E501
        :rtype: CreateBookRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this CreateBookRequest.


        :return: The title of this CreateBookRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this CreateBookRequest.


        :param title: The title of this CreateBookRequest.
        :type title: str
        """

        self._title = title

    @property
    def author(self) -> str:
        """Gets the author of this CreateBookRequest.


        :return: The author of this CreateBookRequest.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this CreateBookRequest.


        :param author: The author of this CreateBookRequest.
        :type author: str
        """

        self._author = author

    @property
    def genres(self) -> List[str]:
        """Gets the genres of this CreateBookRequest.


        :return: The genres of this CreateBookRequest.
        :rtype: List[str]
        """
        return self._genres

    @genres.setter
    def genres(self, genres: List[str]):
        """Sets the genres of this CreateBookRequest.


        :param genres: The genres of this CreateBookRequest.
        :type genres: List[str]
        """

        self._genres = genres

    @property
    def number_of_pages(self) -> int:
        """Gets the number_of_pages of this CreateBookRequest.


        :return: The number_of_pages of this CreateBookRequest.
        :rtype: int
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        """Sets the number_of_pages of this CreateBookRequest.


        :param number_of_pages: The number_of_pages of this CreateBookRequest.
        :type number_of_pages: int
        """

        self._number_of_pages = number_of_pages