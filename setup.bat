@echo off
echo Setting up Ship Booking System Backend...
cd Backend

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Python is not installed or not in PATH. Please install Python.
    pause
    exit /b
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing requirements...
pip install django django-cors-headers

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Populating database with sample data...
python populate_db.py

echo.
echo ==============================================
echo 4. Starting the Django Server...
echo ==============================================
python manage.py runserver

pause
