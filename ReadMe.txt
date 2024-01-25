*** THIS IS THE EXPLANATION OF THIS PROJECT ***


INTRODUCTION

This code is an implementation of GraphQL server using the Ariadne library in Python.
It defines a GraphQL schema and provides resolver functions for querying and mutating data related to Books

...............................................................................................................................

"db.py"

The 'db.py' file contains all the data of this project
or, simply, it is the database of this project.

...............................................................................................................................

"schema.py"

The 'schema.py' file defines the structure of your GraphQL API and
specifies what types of operations can be performed on the data.
It outlines the types, queries, mutations, and input types that are available to users.

In 'schema.py' 'query' is  to return data stored in database.
It defines how users can retrieve data from the GraphQL server.
It specifies the queries that users can use to request data, and provides the structure for those queries.


EXPLANATION OF MUTATION

In 'mutation' we specify the type of operation that can be performed on the database
For eg: there could be: create, read, update , and delete.

In the program I have written types of mutation i.e. adding, updating, and deleting
by passing all the parameters inside the same function which is as follows:

    type Mutation {
            addBook(title: String!, author: String!): Book
            updateBook(id: ID!, title: String!, author: String!): Book
            deleteBook(id: ID!): Book
            }

But if there are many parameters we can write as follows
i.e. by passing arguments separately as a function

    type Mutation {
        addBook(book: AddBookInput!): Book
        updateBook(id: ID!, edits: EditBookInput!): Book
        deleteBook(id: ID!): Book
    }

    input AddBookInput {
        title: String!
        author: String!
    }

    input EditBookInput {
        title: String
        author: String
    }

NOTE : To delete the book we only need id of the book, and we can easily delete
       so, we don't need separate function for this.

       But for adding we need to insert all the elements like id, title, author.
       So, we defined a separate function for that instead of passing all the arguments at once.
       Similarly, for edit/update we may need to update all the fields as well.

...............................................................................................................................

"main.py"

'main.py' is basically used to create a GraphQL API, it helps user communicate with the database.
It serves as the entry point for our GraphQL API server.

It acts as the middleware that handles incoming GraphQL requests, processes them, interacts with the database or data source as needed,
and returns responses to clients.
It effectively serves as the bridge between clients and the database,
allowing users to communicate with and manipulate data using GraphQL queries and mutations.

...............................................................................................................................
