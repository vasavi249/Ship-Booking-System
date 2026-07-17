# Ship Booking System

## Project Description
Ship Booking System is a complete, professional, Full Stack web application designed to manage and automate cruise ship bookings. It provides a seamless experience for passengers to search for ships, view schedules, select cabins, and make payments. It also includes an admin dashboard to manage the entire fleet, schedules, and passenger data.

## Features
- **Passenger Module**: Registration, Login, Dashboard, Booking History.
- **Booking Flow**: Search ships, view details and gallery, select cabin types (Standard, Deluxe, Suite), and generate automatic transaction IDs during payment.
- **Admin Dashboard**: Complete CRUD management for Passengers, Ships, Schedules, Bookings, and Payments.
- **Modern UI/UX**: Professional, responsive design built with CSS Glassmorphism, animations, flexbox, and CSS Grid.
- **API-Driven**: Complete separation of frontend and backend utilizing Django Function-Based Views (returning JSON) and JavaScript Fetch API.

## Technology Stack
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6, Fetch API)
- **Backend**: Python, Django (Function-Based Views)
- **Database**: SQLite (Default Django DB)
- **API Testing**: Postman

## Folder Structure
```text
Ship Booking System/
│
├── Backend/                    # Django Backend Source Code
│   ├── manage.py               # Django execution script
│   ├── populate_db.py          # Script to populate sample data
│   ├── ShipBookingSystem/      # Django Project Config
│   │   ├── settings.py         # Includes CORS setup and apps
│   │   ├── urls.py             # Project URLs
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── booking/                # Django App
│       ├── models.py           # Database Models
│       ├── views.py            # Function Based Views (20 CRUD APIs)
│       ├── urls.py             # API Routes
│       ├── admin.py
│       └── apps.py
│
├── Frontend/                   # Vanilla HTML/CSS/JS Source Code
│   ├── index.html              # Home Page with Hero Banner
│   ├── register.html           # Passenger Registration
│   ├── login.html              # Passenger Login
│   ├── ships.html              # Ship Listing
│   ├── ship_details.html       # Ship Details & Schedules
│   ├── booking.html            # Booking Summary & Cabin Selection
│   ├── payment.html            # Payment Gateway Mock
│   ├── booking_history.html    # Passenger's Trip History
│   ├── passenger_dashboard.html# Passenger Dashboard (Stats)
│   ├── admin_dashboard.html    # Admin Management
│   ├── style.css               # Global Styles (Glassmorphism)
│   └── script.js               # Frontend API Integration (Fetch)
│
├── Postman_Collection.json     # Complete API testing collection
├── setup.bat                   # Windows batch script for automated setup
└── README.md                   # Project Documentation
```

## Installation Steps & Run Server

### Option 1: Automated Setup (Windows)
1. Double-click the `setup.bat` file in the root directory.
2. It will automatically create a virtual environment, install dependencies, run database migrations, populate the database with sample data, and start the Django development server on `http://127.0.0.1:8000`.

### Option 2: Manual Terminal Commands
1. **Navigate to Backend**
   ```bash
   cd Backend
   ```
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install django django-cors-headers
   ```
4. **Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Populate Sample Data**
   ```bash
   python populate_db.py
   ```
6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run Server**
   ```bash
   python manage.py runserver
   ```

## Running the Frontend
The frontend consists of plain HTML/CSS/JS files. You do not need a web server to view them.
1. Simply open `Frontend/index.html` in any modern web browser.
2. Ensure the Django backend server is running (`http://127.0.0.1:8000`) for the API requests to work.

## API Endpoints (Base: `http://127.0.0.1:8000/api/`)
*All endpoints accept and return JSON payloads.*

- **Passengers**: `/passengers/add/` (POST), `/passengers/` (GET), `/passengers/update/<id>/` (PUT), `/passengers/delete/<id>/` (DELETE)
- **Ships**: `/ships/add/` (POST), `/ships/` (GET), `/ships/update/<id>/` (PUT), `/ships/delete/<id>/` (DELETE)
- **Schedules**: `/schedules/add/` (POST), `/schedules/` (GET), `/schedules/update/<id>/` (PUT), `/schedules/delete/<id>/` (DELETE)
- **Bookings**: `/bookings/add/` (POST), `/bookings/` (GET), `/bookings/update/<id>/` (PUT), `/bookings/delete/<id>/` (DELETE)
- **Payments**: `/payments/add/` (POST), `/payments/` (GET), `/payments/update/<id>/` (PUT), `/payments/delete/<id>/` (DELETE)
- **Auth**: `/login/` (POST)

## Screenshots Section (Mockups)
The UI has been built with a modern Glassmorphism aesthetic. By opening the HTML files in your browser, you will see the full layout:
- **Home (`index.html`)**: Features a beautiful ocean background hero section, search form, and featured cruise cards.
- **Register & Login**: Centered glass cards with form validation.
- **Ships & Details**: Grid layouts with Unsplash placeholders representing the ships and their galleries.
- **Booking & Payment**: Split layout for summary and cabin selection, flowing into a styled payment form.
- **Dashboards**: Responsive stat cards with gradient backgrounds and modern data tables.

## API Testing (Postman)
1. Open Postman.
2. Click **Import**.
3. Select the `Postman_Collection.json` file located in the root of this project.
4. The collection contains 21 configured requests with sample JSON bodies for all CRUD operations.

## GitHub Upload Steps
To submit this project via GitHub:
1. Initialize Git in the project root:
   ```bash
   git init
   ```
2. Create a `.gitignore` file and add the following:
   ```text
   Backend/venv/
   Backend/__pycache__/
   Backend/db.sqlite3
   ```
3. Add and commit all files:
   ```bash
   git add .
   git commit -m "Initial commit: Complete Ship Booking System"
   ```
4. Create a new repository on GitHub.
5. Link the remote repository and push:
   ```bash
   git remote add origin <your-repository-url>
   git branch -M main
   git push -u origin main
   ```

## Future Enhancements
- Implement JWT or Session-based authentication for secure API access.
- Add email notifications for booking confirmations using Django's email backend.
- Integrate a real payment gateway (like Stripe or Razorpay) instead of the mock implementation.
- Add advanced filtering (by date, price, ship type) in the search functionality.

## Author
Senior Full Stack Django Developer
#

<img width="1901" height="992" alt="Screenshot 2026-07-17 152646" src="https://github.com/user-attachments/assets/d7c0a863-b557-44e9-b78e-6400526c3f59" />
<img width="1868" height="997" alt="Screenshot 2026-07-17 152611" src="https://github.com/user-attachments/assets/55272034-81ff-4754-8eb6-e111b9747055" />
<img width="1872" height="1042" alt="Screenshot 2026-07-17 152453" src="https://github.com/user-attachments/assets/cfa5e78a-cfe5-4ddb-a71c-8fc033ec5f7e" />
<img width="1887" height="977" alt="Screenshot 2026-07-17 152326" src="https://github.com/user-attachments/assets/4e2c1c94-2e17-467c-9162-8dbf160b371c" />
<img width="1907" height="1037" alt="Screenshot 2026-07-17 160934" src="https://github.com/user-attachments/assets/c6cda962-bf29-4fdb-96b9-8b886bf76049" />
<img width="1865" height="893" alt="Screenshot 2026-07-17 154250" src="https://github.com/user-attachments/assets/d596e06c-fee7-41ed-bd00-d222dc8dfbf3" />
<img width="1871" height="893" alt="Screenshot 2026-07-17 154231" src="https://github.com/user-attachments/assets/bfb1ab85-0ef8-423c-bc28-9342f5265666" />
<img width="1847" height="876" alt="Screenshot 2026-07-17 154210" src="https://github.com/user-attachments/assets/128979ce-5779-48df-95e5-c488ad2ba69d" />
<img width="1877" height="893" alt="Screenshot 2026-07-17 154128" src="https://github.com/user-attachments/assets/f379ca21-514e-493b-964d-9e14f416bdc3" />
