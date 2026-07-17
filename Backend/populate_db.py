import os
import django
from datetime import date, time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShipBookingSystem.settings')
django.setup()

from booking.models import Passenger, Ship, Schedule, Booking, Payment

def populate():
    print("Populating database with sample data...")

    # Passenger
    passenger, created = Passenger.objects.get_or_create(
        email='rahul@example.com',
        defaults={
            'full_name': 'Rahul Sharma',
            'phone': '9876543210',
            'nationality': 'Indian',
            'passport_number': 'A1234567',
            'password': 'password123'
        }
    )
    print(f"Passenger: {passenger.full_name}")

    # Ship
    ship_data = [
        {"name": "Symphony of the Seas", "type": "Luxury Cruiser", "capacity": 6680, "operator": "Royal Caribbean"},
        {"name": "MS Freedom", "type": "Ocean Liner", "capacity": 3782, "operator": "Royal Caribbean"},
        {"name": "AIDAprima", "type": "Expedition", "capacity": 3300, "operator": "AIDA Cruises"},
        {"name": "Genting Dream", "type": "Mega Cruiser", "capacity": 3352, "operator": "Dream Cruises"},
        {"name": "Silver Whisper", "type": "Luxury Yacht", "capacity": 382, "operator": "Silversea"},
        {"name": "Seven Seas Explorer", "type": "Luxury Cruiser", "capacity": 750, "operator": "Regent"},
        {"name": "Seabourn Encore", "type": "Ultra Luxury", "capacity": 600, "operator": "Seabourn"},
        {"name": "Viking Star", "type": "Ocean Liner", "capacity": 930, "operator": "Viking Cruises"},
        {"name": "Crystal Serenity", "type": "Luxury Cruiser", "capacity": 980, "operator": "Crystal Cruises"},
        {"name": "Queen Victoria", "type": "Classic Liner", "capacity": 2061, "operator": "Cunard"},
        {"name": "Celebrity Edge", "type": "Modern Luxury", "capacity": 2918, "operator": "Celebrity Cruises"},
        {"name": "Norwegian Bliss", "type": "Mega Cruiser", "capacity": 4004, "operator": "NCL"},
        {"name": "MSC Meraviglia", "type": "Mega Cruiser", "capacity": 4500, "operator": "MSC Cruises"},
        {"name": "Costa Diadema", "type": "Ocean Liner", "capacity": 4947, "operator": "Costa Cruises"},
        {"name": "Disney Dream", "type": "Family Cruiser", "capacity": 4000, "operator": "Disney Cruise Line"},
        {"name": "Carnival Vista", "type": "Fun Ship", "capacity": 3934, "operator": "Carnival"}
    ]

    for s in ship_data:
        Ship.objects.get_or_create(
            ship_name=s['name'],
            defaults={
                'ship_type': s['type'],
                'capacity': s['capacity'],
                'operator_name': s['operator'],
                'status': 'Active'
            }
        )

    print(f"Ships populated")

    # Generate schedules for all ships
    ports = [
        ("Miami, USA", "Nassau, Bahamas", 36000),
        ("Barcelona, Spain", "Rome, Italy", 68000),
        ("Seattle, USA", "Juneau, Alaska", 96000),
        ("Athens, Greece", "Santorini, Greece", 48000),
        ("Sydney, Australia", "Auckland, New Zealand", 120000),
        ("Southampton, UK", "New York, USA", 144000),
        ("Dubai, UAE", "Mumbai, India", 96000),
        ("Vancouver, Canada", "Ketchikan, Alaska", 88000)
    ]

    import random
    random.seed(42) # For reproducible results

    for idx, s in enumerate(ship_data):
        port_route = ports[idx % len(ports)]
        Schedule.objects.get_or_create(
            ship_name=s['name'],
            source_port=port_route[0],
            destination_port=port_route[1],
            defaults={
                'departure_date': date(2026, 10 + (idx % 3), 5 + (idx % 20)),
                'departure_time': time(10 + (idx % 8), 0),
                'arrival_date': date(2026, 10 + (idx % 3), 7 + (idx % 20)),
                'arrival_time': time(8 + (idx % 5), 0),
                'fare': port_route[2]
            }
        )

    print(f"Schedules populated for ALL ships")

    # Booking
    booking, created = Booking.objects.get_or_create(
        passenger_name='Rahul Sharma',
        ship_name='Symphony of the Seas',
        defaults={
            'cabin_type': 'Suite',
            'journey_date': date(2026, 8, 15),
            'source_port': 'Chennai Port',
            'destination_port': 'Port Blair',
            'total_amount': 1000.00,
            'booking_status': 'Confirmed'
        }
    )
    print(f"Booking: {booking.booking_id} - {booking.booking_status}")

    # Payment
    payment, created = Payment.objects.get_or_create(
        transaction_id='TXN987654321',
        defaults={
            'booking_id': booking.booking_id,
            'passenger_name': 'Rahul Sharma',
            'amount': 1000.00,
            'payment_method': 'Credit Card',
            'payment_status': 'Success'
        }
    )
    print(f"Payment: {payment.transaction_id} - {payment.payment_status}")
    print("Database population complete!")

if __name__ == '__main__':
    populate()
