const BASE_URL = 'http://127.0.0.1:8000/api';

// --- Utilities ---
function showAlert(message, type = 'success') {
    const alertBox = document.getElementById('alertBox');
    if (alertBox) {
        alertBox.textContent = message;
        alertBox.className = `alert alert-${type}`;
        alertBox.style.display = 'block';
        setTimeout(() => alertBox.style.display = 'none', 3000);
    } else {
        alert(message);
    }
}

// Get logged-in user from localStorage
function getCurrentUser() {
    return JSON.parse(localStorage.getItem('passenger'));
}

// Check auth for protected pages
function checkAuth() {
    if (!getCurrentUser()) {
        window.location.href = 'login.html';
    }
}

// Logout function
function logout() {
    localStorage.removeItem('passenger');
    window.location.href = 'index.html';
}

// Ensure navbar shows correct auth state
function updateNavbar() {
    const user = getCurrentUser();
    const navLinks = document.getElementById('nav-links');
    if (navLinks) {
        if (user) {
            navLinks.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="ships.html">Ships</a></li>
                <li><a href="passenger_dashboard.html">Dashboard</a></li>
                <li><a href="#" onclick="logout()">Logout (${user.full_name})</a></li>
            `;
        } else {
            navLinks.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="ships.html">Ships</a></li>
                <li><a href="login.html" class="nav-btn">Login</a></li>
                <li><a href="register.html" class="nav-btn" style="background:var(--secondary)">Register</a></li>
            `;
        }
    }
}

document.addEventListener('DOMContentLoaded', updateNavbar);

// --- API Calls ---

// Register Passenger
async function registerPassenger(data) {
    try {
        const response = await fetch(`${BASE_URL}/passengers/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (response.ok) {
            showAlert('Registration successful! Please login.', 'success');
            setTimeout(() => window.location.href = 'login.html', 2000);
        } else {
            showAlert(result.error || 'Registration failed', 'error');
        }
    } catch (error) {
        showAlert('Network error occurred', 'error');
    }
}

// Login
async function login(email, password) {
    try {
        const response = await fetch(`${BASE_URL}/login/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const result = await response.json();
        if (response.ok) {
            localStorage.setItem('passenger', JSON.stringify(result));
            showAlert('Login successful!', 'success');
            setTimeout(() => window.location.href = 'passenger_dashboard.html', 1000);
        } else {
            showAlert(result.error || 'Invalid credentials', 'error');
        }
    } catch (error) {
        showAlert('Network error occurred', 'error');
    }
}

// Fetch Ships
async function fetchShips() {
    try {
        const response = await fetch(`${BASE_URL}/ships/`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching ships", error);
        return [];
    }
}

// Fetch Schedules
async function fetchSchedules() {
    try {
        const response = await fetch(`${BASE_URL}/schedules/`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching schedules", error);
        return [];
    }
}

// Create Booking
async function createBooking(data) {
    try {
        const response = await fetch(`${BASE_URL}/bookings/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (response.ok) {
            localStorage.setItem('currentBooking', JSON.stringify({id: result.id, ...data}));
            window.location.href = 'payment.html';
        } else {
            showAlert('Booking failed: ' + result.error, 'error');
        }
    } catch (error) {
        showAlert('Network error during booking', 'error');
    }
}

// Create Payment
async function createPayment(data) {
    try {
        const response = await fetch(`${BASE_URL}/payments/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (response.ok) {
            showAlert('Payment successful! Redirecting...', 'success');
            setTimeout(() => window.location.href = 'booking_history.html', 2000);
        } else {
            showAlert('Payment failed: ' + result.error, 'error');
        }
    } catch (error) {
        showAlert('Network error during payment', 'error');
    }
}

// Generic Fetch for Admin Dashboard
async function fetchAny(endpoint) {
    const res = await fetch(`${BASE_URL}/${endpoint}/`);
    return await res.json();
}

async function deleteAny(endpoint, id) {
    const res = await fetch(`${BASE_URL}/${endpoint}/delete/${id}/`, { method: 'DELETE' });
    return await res.json();
}
