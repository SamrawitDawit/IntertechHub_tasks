# Published postman documentation: `https://documenter.getpostman.com/view/33567770/2sAYBYhB5z`


# Auth Signup
This endpoint allows the user to sign up by providing a username, password, and role in the request body.
## Request Body
* username (string) - The username of the user.
* password (string) - The password for the user account.
* role (string) - The role of the user (e.g., admin, user).

## Response
Upon successful signup, the server returns a status code of 201 and a JSON response with a message indicating the success of the signup process.
Example:


```JSON
{
    "message": "user created successfully"
}
```

# Auth Login
This endpoint is used to authenticate a user and obtain an access token.
## Request Body
* username (string, required): The username of the user.
* password (string, required): The password of the user.

## Response
The response is in JSON format with the following schema:


``` JSON
{
  "type": "object",
  "properties": {
    "access_token": {
      "type": "string"
    }
  }
}
```

The response contains an access token as a string.


# Add New Book
This endpoint allows you to add a new book to the database.
## Request Body
* title (string, required): The title of the book.
* author (string, required): The author of the book.
* isbn (string, required): The ISBN of the book.
* published_year (integer, required): The year the book was published.

## Response
The response is in JSON format with the following schema:


```JSON
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    }
}
```

## Example
Request:

```JSON
{
    "title": "Title",
    "author": "Name",
    "isbn": "1234567890123",
    "published_year": 2023
}
```
Response:

```JSON
{
    "message": "Book added"
}
```


# Update Book Details
This endpoint allows the client to update the details of a specific book using its unique identifier.
## Request Body
* title (string) - The updated title of the book.
* author (string) - The updated author of the book.
* isbn (string) - The updated ISBN of the book.
* published_year (number) - The updated published year of the book.

## Response
The response will be in JSON format with the following schema:

```JSON
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    }
}
```
The response will include a message indicating the status of the update operation.


# Delete Book

The HTTP DELETE request is used to delete a specific book with the given ID. Upon successful deletion, the API returns a JSON response with a status code of 200 and a message indicating the success of the operation.

### Response

The response for this request can be documented as a JSON schema:

``` json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    }
}

 ```

### GET /books

This endpoint retrieves a list of books.

#### Request

There are no request parameters for this endpoint.

#### Response

The response is in JSON format and returns an array of book objects. Each book object has the following properties:

- `_id` (string): The unique identifier of the book.
    
- `author` (string): The name of the author of the book.
    
- `isbn` (string): The International Standard Book Number (ISBN) of the book.
    
- `published_year` (number): The year in which the book was published.
    
- `title` (string): The title of the book.
    

Example response:

``` json
[
    {
        "_id": "",
        "author": "",
        "isbn": "",
        "published_year": 0,
        "title": ""
    }
]

 ```

 # Get All Books(Admin only)

This endpoint makes an HTTP GET request to retrieve all the books. The request does not require any parameters in the request body or URL. The response will be in JSON format with an array of objects, each representing a book. Each book object will have properties like `_id`, `author`, `isbn`, `published_year`, and `title`. The values for these properties will be specific to each book in the database.

### GET /books/Name

This endpoint retrieves information about a book based on its name.

#### Request

No request body is required for this endpoint.

#### Response

The response will be a JSON array containing information about the book. Each object in the array will have the following properties:

- `_id` (string): The unique identifier of the book.
    
- `author` (string): The name of the author of the book.
    
- `isbn` (string): The ISBN of the book.
    
- `published_year` (number): The year in which the book was published.
    
- `title` (string): The title of the book.
    

#### Example Response

``` json
[
    {
        "_id": "",
        "author": "",
        "isbn": "",
        "published_year": 0,
        "title": ""
    }
]

 ```

 ### Add Book Takeaway

This endpoint allows the user to add a takeaway for a specific book.

#### Request Body

- takeaway (string, required): The takeaway to be added for the book.
    

#### Response (201 - Created)

The response will be in JSON format with the following schema:

``` json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    }
}

 ```

 ### GET /books/{bookId}/takeaways

This endpoint retrieves the takeaways for a specific book identified by the `bookId`.

#### Request

No request body is required for this endpoint.

- `bookId` (path parameter) : The unique identifier of the book for which takeaways are to be retrieved.
    

#### Response

The response will be a JSON object with the following schema:

``` json
{
    "takeaways": {
        "type": "array",
        "items": {
            "type": "string"
        }
    }
}

 ```

The response will contain an array of takeaways for the specified book. Each takeaway is represented as a string.

Example response:

``` json
{
    "takeaways": [
        "Example takeaway 1",
        "Example takeaway 2"
    ]
}

 ```



