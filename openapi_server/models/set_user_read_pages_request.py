from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class SetUserReadPagesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, book_id=None, pages_read=None):  # noqa: E501
        """SetUserReadPagesRequest - a model defined in OpenAPI

        :param book_id: The book_id of this SetUserReadPagesRequest.  # noqa: E501
        :type book_id: str
        :param pages_read: The pages_read of this SetUserReadPagesRequest.  # noqa: E501
        :type pages_read: int
        """
        self.openapi_types = {
            'book_id': str,
            'pages_read': int
        }

        self.attribute_map = {
            'book_id': 'bookId',
            'pages_read': 'pagesRead'
        }

        self._book_id = book_id
        self._pages_read = pages_read

    @classmethod
    def from_dict(cls, dikt) -> 'SetUserReadPagesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The set_user_read_pages_request of this SetUserReadPagesRequest.  # noqa: E501
        :rtype: SetUserReadPagesRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def book_id(self) -> str:
        """Gets the book_id of this SetUserReadPagesRequest.


        :return: The book_id of this SetUserReadPagesRequest.
        :rtype: str
        """
        return self._book_id

    @book_id.setter
    def book_id(self, book_id: str):
        """Sets the book_id of this SetUserReadPagesRequest.


        :param book_id: The book_id of this SetUserReadPagesRequest.
        :type book_id: str
        """

        self._book_id = book_id

    @property
    def pages_read(self) -> int:
        """Gets the pages_read of this SetUserReadPagesRequest.


        :return: The pages_read of this SetUserReadPagesRequest.
        :rtype: int
        """
        return self._pages_read

    @pages_read.setter
    def pages_read(self, pages_read: int):
        """Sets the pages_read of this SetUserReadPagesRequest.


        :param pages_read: The pages_read of this SetUserReadPagesRequest.
        :type pages_read: int
        """

        self._pages_read = pages_read
