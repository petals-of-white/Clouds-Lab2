from uuid import UUID, uuid4
from pydantic import StrictStr
from openapi_server.models import Author, Book, User, Genre


authors : list[Author] = [Author(uuid4(), 'Lorem', 'Ipsum'), Author(uuid4(), 'Hello', 'World')]
genres: list[Genre] = [Genre(uuid4(), 'GenreA'), Genre(uuid4(), 'GenreB'), Genre(uuid4(), 'GenreC')]

books : list[Book] = [
    Book(uuid4(), 'Book1', 100, [genres[0]], authors[0].id),
    Book(uuid4(), 'Book2', 300, [genres[0], genres[1]], authors[1].id),
    Book(uuid4(), 'Book3', 123, [genres[0], genres[2]], authors[1].id)]

users: list[User] = [User(uuid4(), 'Green', 'Crocodile'), User('Mighty', 'Lion'), User('Big', 'Hippo')]

userBooks: list[tuple[str, str, int]] = [
    (users[0], books[0], 20),
    (users[0], books[1], 100),
    (users[1], books[1], 99),
    (users[2], books[2], 113),
    (users[2], books[0], 10)
]
