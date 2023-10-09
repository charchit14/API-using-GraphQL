from ariadne import ObjectType, QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from schema import type_def
import db as db

# Creating query, mutation, and object types
# In this section, instances of QueryType, MutationType, and ObjectType are created to structure the GraphQL schema
# query, mutation, and book are variables that will hold the definitions for the query, mutation, and Book object types
query = QueryType()
mutation = MutationType()
book = ObjectType("Book")


# Resolver function to retrieve all the books
# Resolver functions are responsible for fetching data when a client sends a query.
# Resolver function for the getBooks query: This section defines a resolver function for the getBooks query field.
# In this case, it simply returns the list of books from the db.books data source.
@query.field('getBooks')
def resolve_get_books(_, info):
    return db.books


# Resolver function to retrieve book by its ID
@query.field('getBookByID')
def resolve_get_book_by_id(_, info, id):
    return next((b for b in db.books if b["id"] == id), None)


# Resolver function to retrieve a book by its title
@query.field('getBookByTitle')
def resolve_get_book_by_title(_, info, title):
    return next((b for b in db.books if b["title"] == title), None)


# Resolver function to retrieve a book by its Author
@query.field('getBookByAuthor')
def resolve_get_book_by_author(_, info, author):
    return next((b for b in db.books if b["author"] == author), None)


# Resolver function to add a new book
# This section defines a resolver function for the 'addBook' mutation field
@mutation.field('addBook')
def resolve_add_book(_, info, title, author):
    new_book = {
        "id": str(len(db.books) + 1),
        "title": title,
        "author": author
    }
    db.books.append(new_book)
    return new_book


# Resolver function to update an existing book
@mutation.field('updateBook')
def resolve_update_book(_, info, id, title, author):
    for b in db.books:
        if b["id"] == id:
            b["title"] = title
            b["author"] = author
            return b
    return None


# Resolver function to delete a book by its ID
@mutation.field('deleteBook')
def resolve_delete_book(_, info, id):
    for b in db.books:
        if b["id"] == id:
            deleted_book = db.books.pop(db.books.index(b))
            return deleted_book
    return None


# Creating an executable schema
# This function combines the schema definition (type_def) with
# query, mutation, and object types (query, mutation, book) that were defined earlier.
# It creates a complete schema that includes the queries, mutations, and types we've defined.
schema = make_executable_schema(type_def, query, mutation, book)


# Creating a Starlette app and mounting the GraphQL schema
app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))
