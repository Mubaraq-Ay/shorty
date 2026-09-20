# Shorty

A simple URL shortener built from scratch in Python, using only the standard library and SQLite.

Shorty takes a long URL, generates a unique short code, stores the mapping in SQLite, and runs a local HTTP server that redirects short URLs to their original destinations.

## Features

* URL validation
* Random 6-character short codes
* Collision checking
* SQLite database storage
* HTTP server built with Python's `http.server`
* HTTP 302 redirects
* HTTP 404 handling for unknown short codes

## Tech Stack

* Python
* SQLite
* Python Standard Library

  * `urllib.parse`
  * `secrets`
  * `sqlite3`
  * `http.server`

No web framework is used.

## How It Works

### Creating a Short URL

The user provides a URL. Shorty validates that it uses `http` or `https`, then generates a random 6-character code.

The code is checked against the database to make sure it isn't already being used.

The URL and short code are then stored in SQLite.

### Redirecting

When the server receives a request such as:

```text
GET /uaBzjY
```

Shorty extracts the short code and searches the database.

If the code exists, the server responds with:

```text
HTTP 302
Location: <original URL>
```

The browser then follows the redirect.

If the code doesn't exist, the server responds with:

```text
HTTP 404
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Mubaraq-Ay/shorty.git
cd url-shortner
```

### 2. Create a short URL

Run:

```bash
python main.py
```

Choose:

```text
1. Shorten URL
```

Enter a valid URL.

Shorty will return a 6-character short code.

### 3. Start the server

Run:

```bash
python server.py
```

The server runs on:

```text
http://localhost:8000
```

Visit:

```text
http://localhost:8000/<short-code>
```

to be redirected to the original URL.

## Project Structure

```text
url-shortner/
├── main.py       # URL creation and database storage
├── server.py     # HTTP server and redirects
├── .gitignore
└── README.md
```

## Why I Built This

Shorty was built as a fundamentals project to understand what happens underneath backend frameworks.

The project focuses on learning:

* HTTP requests and responses
* HTTP status codes
* Redirects
* URL parsing
* SQLite
* SQL queries
* Random token generation
* Basic request handling
* Connecting a database to an HTTP server

It intentionally avoids frameworks so the underlying concepts are easier to understand.

## Limitations

This is a learning project, not a production-ready URL shortener.

It currently has no:

* Authentication
* Analytics
* Custom aliases
* Rate limiting
* Expiration
* Frontend
* Production deployment

These are intentionally outside the scope of the project.
