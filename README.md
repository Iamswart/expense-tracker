The Expense Tracker API is a Django Rest Framework application that allows users to manage their expenses, categorize them, set budgets for each category, and view analytics regarding their spending habits. This application uses JWT for authentication and provides endpoints for user registration, expense management, budget management, and analytics.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8+
pip
Virtualenv (optional)

Installation
Clone the repository
git clone https://github.com/Iamswart/expense-tracker
cd expense-tracker

Create and activate a virtual environment (optional)
virtualenv myenv

# On Windows

myenv\Scripts\activate

# On Unix or MacOS

source myenv/bin/activate

Install the required packages
pip install -r requirements.txt

Set up environment variables
Create a .env file in the root directory of the project and add the following variables:

DEBUG=True
DJANGO_SECRET_KEY='your_secret_key'
DATABASE_NAME='your_db_name'
DATABASE_USER='your_db_user'
DATABASE_PASSWORD='your_db_password'
DATABASE_HOST='your_db_host'
DATABASE_PORT='your_db_port'
Replace the placeholders with your actual database configuration and Django secret key.

Run database migrations
python manage.py migrate

Start the development server
python manage.py runserver
The API will be available at http://localhost:8000/api/.

Using the API
User Registration
To create a new user:

Endpoint: /api/users/register/
Method: POST
Data: {"username": "yourusername", "password": "yourpassword"}
Use the refresh and access tokens provided upon successful user registration.

Authentication

To obtain a JWT access token:
Endpoint: /api/token/
Method: POST
Data: {"username": "yourusername", "password": "yourpassword"}

To obtain a new JWT access token:
Endpoint: /api/token/refresh
Method: POST
Data: {"refresh": "yourrefreshtoken"}


Endpoints
Expenses: /api/expenses/ (GET, POST, PUT, DELETE)
Budgets: /api/budgets/ (GET, POST, PUT, DELETE)
Analytics: /api/analytics/ (GET)
Authentication is required for accessing these endpoints. Include the JWT access token in the Authorization header as follows: Authorization: Bearer <your_access_token>.

Categories: /api/categories/ (GET, POST, PUT, DELETE)
Permissions:
List Categories: Available to all authenticated users.
Create, Update, and Delete Categories: Restricted to admin users only.

Analytics
To view analytics, send a GET request to /api/analytics/ with optional start_date and end_date query parameters in the format YYYY-MM-DD.

Documentation
Swagger UI
The API documentation can be viewed through the Swagger UI, which provides an interactive documentation browser.

Endpoint: /documentation/
Access: Open a web browser and navigate to http://localhost:8000/documentation/ to view the API documentation and interact with the API endpoints directly.