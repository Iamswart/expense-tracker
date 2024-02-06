# Expense Tracker API

The Expense Tracker API is a Django Rest Framework application that allows users to manage their expenses, categorize them, set budgets for each category, and view analytics regarding their spending habits. This application uses JWT for authentication and provides endpoints for user registration, expense management, budget management, and analytics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Iamswart/expense-tracker
   cd expense-tracker

2. **Create and activate a virtual environment windows (optional)**
    ```bash
    virtualenv myenv
    myenv\Scripts\activate

3. **Create and activate a virtual environment Unix or MacOS (optional)**
    ```bash
    virtualenv myenv
    source myenv/bin/activate

4. **Install requirements**
    ```bash
    pip install -r requirements.txt

5. **Set up environment variables**

    Create a .env file in the root directory of the project and add the following variables:

    ```bash
    DEBUG=True
    DJANGO_SECRET_KEY='your_secret_key'
    DATABASE_NAME='your_db_name'
    DATABASE_USER='your_db_user'
    DATABASE_PASSWORD='your_db_password'
    DATABASE_HOST='your_db_host'
    DATABASE_PORT='your_db_port'

    Replace the placeholders with your actual database configuration and Django secret key.

6. **Run database migrations**
    ```bash
    python manage.py migrate

7. **Start the development server**
    ```bash
    python manage.py runserver

    The API will be available at http://localhost:8000/api/.

## Using the API

### User Registration

To create a new user:

- Endpoint: /api/users/register/
- Method: POST
- Data: {"username": "yourusername", "password": "yourpassword"}

### Authentication

To obtain a JWT access token:

- Endpoint: /api/token/
- Method: POST
- Data: {"username": "yourusername", "password": "yourpassword"}

To refresh a JWT access token:

- Endpoint: /api/token/refresh/
- Method: POST
- Data: {"refresh": "yourrefreshtoken"}

### Endpoints

- Expenses: /api/expenses/ (GET, POST, PUT, DELETE)
- Budgets: /api/budgets/ (GET, POST, PUT, DELETE)
- Categories: /api/categories/ (GET, POST, PUT, DELETE)
- Permissions:
   - List Categories: Available to all authenticated users.
   - Create, Update, and Delete Categories: Restricted to admin users only.
- Analytics: /api/analytics/ (GET)

Include the JWT access token in the Authorization header as follows: Authorization: Bearer <your_access_token>.

### Analytics

To view analytics, send a GET request to /api/analytics/ with optional start_date and end_date query parameters in the format YYYY-MM-DD.

### Documentation

Swagger UI

The API documentation can be viewed through the Swagger UI.

- Endpoint: /documentation/
- Access: Open a web browser and navigate to http://localhost:8000/documentation/ to view the API documentation and interact with the API endpoints directly.


## JWT Authentication Process

This application utilizes JSON Web Tokens (JWT) for handling user authentication. The process is straightforward and ensures secure access to the API endpoints.

### Registration

New users can register by providing a username and password. Upon successful registration, the application generates a JWT refresh token and access token pair. The refresh token can be used to obtain new access tokens.

### Obtaining Access Tokens

Users can obtain access tokens by sending their username and password to the /api/token/ endpoint. The response includes both an access token and a refresh token. The access token is used in the Authorization header for subsequent API requests.

### Refreshing Access Tokens

When an access token expires, users can obtain a new access token by sending the refresh token to the /api/token/refresh/ endpoint. This ensures users remain authenticated without needing to provide their username and password again.

### Implementation Highlights

#### User Registration

- The RegisterView allows new users to register by creating a new User instance. It utilizes Django's built-in User model and validate_password method for password validation, ensuring adherence to security best practices.

#### Serializer Validation

- The RegisterSerializer ensures that the username is unique and the password meets Django's validation criteria. It provides clear error messages for validation failures, enhancing the user experience

#### JWT Tokens for Authentication

- The application uses rest_framework_simplejwt for handling JWT tokens, a secure and widely adopted standard for API authentication. This choice simplifies token management and integrates seamlessly with Django Rest Framework.


