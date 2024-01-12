# Flask-Restful-Include-JWT

- [Flask-Restful-Include-JWT](#flask-restful-include-jwt)
  - [Description:](#description)
  - [Features:](#features)
  - [Project Structure](#project-structure)
  - [Getting Started:](#getting-started)
  - [Usage:](#usage)
- [Contributing:](#contributing)
- [References:](#references)

## Description:

Welcome to the Flask-Restful-Include-JWT repository! This project serves as a comprehensive guide and example setup for creating a Flask RESTful API with included JSON Web Token (JWT) authentication.

## Features:

1. Flask-Restful Integration: My Learn documentation how to build RESTful APIs with Flask, a powerful extension for Flask that adds support for quickly building REST APIs.

2. JWT Authentication: Explore the integration of JSON Web Tokens (JWT) for secure and stateless authentication in Flask application. Understand the principles of token-based authentication and how to implement them in this my first Flask RESTful project.

3. Code Organization: The repository provides a well-organized project structure, including modularization of code for better maintainability. Learn best practices for structuring your Flask RESTful projects, i build this just like my javascipt project used nest js but in separate way.

4. Database Integration: Learn how to integrate a database into your Flask RESTful API. The project uses mongoDB, a NoSQL database, and mongoengine, an object-document mapper (ODM), to provide a database backend for the API.

## Project Structure

```arduino
├── src
│   ├── config
│   │   ├── __init__.py
│   │   └── database
│   │       └── database_config.py
│   ├── controller
│   ├── dto
│   ├── helper
│   ├── middleware
│   ├── service
│   ├── route
│   ├── app.py
├── requirements.txt
└── wsgi.py
```

- **config**: Configuration settings for the project, including database configurations in the database subdirectory.
- **controller**: Acts as a bridge between services and requests, handling validation, data serialization, and more using related DTOs.
- **dto**: Data Transfer Objects (DTOs) that define the structure of data exchanged between different layers of the application.
- **helper**: Utility functions and modules that assist in various tasks throughout the project.
- **middleware**: Middleware components that can intercept and process requests before they reach the route handlers.
- **service**: The main business logic of the application. This is where you implement the core functionality of your API.
- **route**: Defines the routes and endpoints of your API.
- **app**.py: The main entry point of your Flask application.
- **requirements.txt**: Lists the dependencies required for the project. You can install them using pip install -r requirements.txt.
- **wsgi.py**: The entry point for running your application using a WSGI server.

## Getting Started:

Clone the repository:

```bash
git clone https://github.com/your-username/flask-restful-include-jwt.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Follow the documentation to set up your Flask RESTful API with JWT authentication.

## Usage:

Run the Flask application:

```bash
python wsgi.py
```

**Have Fun Exploring 😊**:
Access your API at http://localhost:5000/ and play around with the endpoints. It's that simple!

# Contributing:

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open an issue or submit a pull request.

# References:

- [Flask](https://flask-restful.readthedocs.io/en/latest/)
- [PyDantic](https://pydantic-docs.helpmanual.io/)
- [MongoDB](https://docs.mongodb.com/)
