from uuid import UUID
from pydantic import StrictStr
from openapi_server.models import Author, Book, User, Genre


authors : list[Author] = []
books : list[Book] = []
users: list[User] = []
genres: list[Genre] = []

userBooks: list[tuple[str, str, int]] = []
