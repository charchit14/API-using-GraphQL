# This program defines the database and type of operations that can be performed on the database
# Here, ! at the end of built-in data types denotes that it can't be empty/null

type_def = """

    type Book {
        id: ID! 
        title: String!
        author: String!
        }

    type Query {
        getBooks: [Book] 
        getBookByID(id: ID!): Book
        getBookByTitle(title: String!): Book
        getBookByAuthor(author: String!): Book
        }
        
    type Mutation {
        addBook(title: String!, author: String!): Book
        updateBook(id: ID!, title: String!, author: String!): Book
        deleteBook(id: ID!): Book
        }
"""
