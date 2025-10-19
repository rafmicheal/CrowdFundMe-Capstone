Project Overview

CrowdFundMe is a crowdfunding web application that allows users to create and support fundraising projects. The platform connects creators who need funding for their ideas with supporters who believe in them. It is built with Django REST Framework and demonstrates how to manage user authentication, project creation, pledging, and funding logic using APIs.

Features

User registration and authentication

Create and manage crowdfunding projects

Make pledges to support projects

View project details and total pledges

Secure data management with Django REST Framework

Admin interface for managing users and projects

Technologies Used

Python 3

Django 5

Django REST Framework

SQLite (development database)

Git & GitHub for version control

Installation and Setup

Follow these steps to run the project locally:

Clone the repository

git clone https://github.com/rafmicheal/CrowdFundMe-Capstone.git
cd CrowdFundMe-Capstone


Create and activate a virtual environment

python -m venv venv
source venv/Scripts/activate   # For Windows
source venv/bin/activate       # For macOS/Linux


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Run the development server

python manage.py runserver


Access the application
Open your browser and go to http://127.0.0.1:8000/

API Endpoints
Endpoint	Method	Description
/api/projects/	GET	List all projects
/api/projects/	POST	Create a new project
/api/projects/<id>/	GET	Retrieve a single project
/api/projects/<id>/	PUT	Update a project
/api/projects/<id>/pledge/	POST	Make a pledge to a project
Challenges and Solutions

During development, I encountered challenges with route configuration and REST API authentication. I resolved them by carefully reviewing Django’s URL routing system, testing API endpoints with Postman, and debugging through the Django shell.

Next Steps

Add user profiles and authentication via tokens

Implement project progress tracking

Improve front-end integration

Author

Raf Micheal
Developer – Django REST Framework

GitHub: rafmicheal
