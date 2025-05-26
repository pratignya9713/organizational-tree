# Organization Tree

A web application to manage and visualize an organizational hierarchy using Django and ReactJS.

## Features

- Display an organizational tree structure
- Add, edit, view, and delete persons in the organization
- Visual representation of the hierarchy
- RESTful API for data operations

## Technical Stack

- **Backend**: Django + Django REST Framework
- **Frontend**: ReactJS (served directly from Django templates)
- **Database**: SQLite (default)
- **Styling**: Bootstrap

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py makemigrations people
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```
7. Access the application at http://127.0.0.1:8000/
   
## API Endpoints

- `GET /api/people/`: List all people
- `POST /api/people/`: Create a new person
- `GET /api/people/{id}/`: Retrieve a specific person
- `PUT /api/people/{id}/`: Update a specific person
- `DELETE /api/people/{id}/`: Delete a specific person
- `GET /api/people/tree/`: Get the organizational tree structure

## Error Handling

The application implements proper error handling to ensure robustness and user-friendly error messages.

## Code Reusability

The application is designed with code reusability in mind, using Django's class-based views and serializers to maintain DRY principles. 