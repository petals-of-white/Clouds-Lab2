import threading
from uuid import UUID
from pydantic import StrictStr
from openapi_server.models import Author, Book, User, Genre

db_lock = threading.Lock()

authors : list[Author] = []
books : list[Book] = []
users: list[User] = []
genres: list[Genre] = []

userBooks: list[tuple[str, str, int]] = []
