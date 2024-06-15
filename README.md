# Attendance-with-Image-Capture

## Setup
# Clone the repository

git clone https://github.com/pshiv24/Attendance-with-Image-Capture.git
cd attendance

# Create a folder attendance_images for storing images for marking attendance
    attendance/attendance_images

1. Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate

2. Install dependencies:
    pip install -r requirements.txt

3. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

4. Create a superuser:

    python manage.py createsuperuser
    
5. Start the server:
    
    python manage.py runserver
   

API Endpoints
Roster Management:

GET /api/rosters/: List all roster entries.
POST /api/rosters/: Add a new roster entry.
GET /api/rosters/<id>/: Retrieve details of a roster entry.
PUT /api/rosters/<id>/: Update details of a roster entry.
DELETE /api/rosters/<id>/: Delete a roster entry.

Attendance Management:

GET /api/assigned-shifts/: Retrieve assigned shifts for the logged-in user.
POST /api/attendance/: Mark attendance by capturing an image (requires image upload).
