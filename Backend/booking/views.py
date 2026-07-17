from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Passenger, Ship, Schedule, Booking, Payment

def parse_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return {}

# ==========================================
# PASSENGER APIS
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def add_passenger(request):
    data = parse_json(request)
    try:
        passenger = Passenger.objects.create(
            full_name=data.get('full_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            nationality=data.get('nationality'),
            passport_number=data.get('passport_number'),
            password=data.get('password')
        )
        return JsonResponse({'message': 'Passenger added successfully', 'id': passenger.passenger_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def get_passengers(request):
    passengers = list(Passenger.objects.values())
    return JsonResponse(passengers, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_passenger(request, id):
    data = parse_json(request)
    try:
        passenger = Passenger.objects.get(passenger_id=id)
        for key, value in data.items():
            setattr(passenger, key, value)
        passenger.save()
        return JsonResponse({'message': 'Passenger updated successfully'})
    except Passenger.DoesNotExist:
        return JsonResponse({'error': 'Passenger not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_passenger(request, id):
    try:
        passenger = Passenger.objects.get(passenger_id=id)
        passenger.delete()
        return JsonResponse({'message': 'Passenger deleted successfully'})
    except Passenger.DoesNotExist:
        return JsonResponse({'error': 'Passenger not found'}, status=404)

# ==========================================
# SHIP APIS
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def add_ship(request):
    data = parse_json(request)
    try:
        ship = Ship.objects.create(
            ship_name=data.get('ship_name'),
            ship_type=data.get('ship_type'),
            capacity=data.get('capacity'),
            operator_name=data.get('operator_name'),
            status=data.get('status', 'Active')
        )
        return JsonResponse({'message': 'Ship added successfully', 'id': ship.ship_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def get_ships(request):
    ships = list(Ship.objects.values())
    return JsonResponse(ships, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_ship(request, id):
    data = parse_json(request)
    try:
        ship = Ship.objects.get(ship_id=id)
        for key, value in data.items():
            setattr(ship, key, value)
        ship.save()
        return JsonResponse({'message': 'Ship updated successfully'})
    except Ship.DoesNotExist:
        return JsonResponse({'error': 'Ship not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ship(request, id):
    try:
        ship = Ship.objects.get(ship_id=id)
        ship.delete()
        return JsonResponse({'message': 'Ship deleted successfully'})
    except Ship.DoesNotExist:
        return JsonResponse({'error': 'Ship not found'}, status=404)

# ==========================================
# SCHEDULE APIS
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def add_schedule(request):
    data = parse_json(request)
    try:
        schedule = Schedule.objects.create(
            ship_name=data.get('ship_name'),
            source_port=data.get('source_port'),
            destination_port=data.get('destination_port'),
            departure_date=data.get('departure_date'),
            departure_time=data.get('departure_time'),
            arrival_date=data.get('arrival_date'),
            arrival_time=data.get('arrival_time'),
            fare=data.get('fare')
        )
        return JsonResponse({'message': 'Schedule added successfully', 'id': schedule.schedule_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def get_schedules(request):
    schedules = list(Schedule.objects.values())
    return JsonResponse(schedules, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_schedule(request, id):
    data = parse_json(request)
    try:
        schedule = Schedule.objects.get(schedule_id=id)
        for key, value in data.items():
            setattr(schedule, key, value)
        schedule.save()
        return JsonResponse({'message': 'Schedule updated successfully'})
    except Schedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_schedule(request, id):
    try:
        schedule = Schedule.objects.get(schedule_id=id)
        schedule.delete()
        return JsonResponse({'message': 'Schedule deleted successfully'})
    except Schedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)

# ==========================================
# BOOKING APIS
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def add_booking(request):
    data = parse_json(request)
    try:
        booking = Booking.objects.create(
            passenger_name=data.get('passenger_name'),
            ship_name=data.get('ship_name'),
            cabin_type=data.get('cabin_type'),
            journey_date=data.get('journey_date'),
            source_port=data.get('source_port'),
            destination_port=data.get('destination_port'),
            total_amount=data.get('total_amount'),
            booking_status=data.get('booking_status', 'Confirmed')
        )
        return JsonResponse({'message': 'Booking added successfully', 'id': booking.booking_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def get_bookings(request):
    bookings = list(Booking.objects.values())
    return JsonResponse(bookings, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_booking(request, id):
    data = parse_json(request)
    try:
        booking = Booking.objects.get(booking_id=id)
        for key, value in data.items():
            setattr(booking, key, value)
        booking.save()
        return JsonResponse({'message': 'Booking updated successfully'})
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_booking(request, id):
    try:
        booking = Booking.objects.get(booking_id=id)
        booking.delete()
        return JsonResponse({'message': 'Booking deleted successfully'})
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)

# ==========================================
# PAYMENT APIS
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def add_payment(request):
    data = parse_json(request)
    try:
        payment = Payment.objects.create(
            booking_id=data.get('booking_id'),
            passenger_name=data.get('passenger_name'),
            amount=data.get('amount'),
            payment_method=data.get('payment_method'),
            payment_status=data.get('payment_status', 'Success'),
            transaction_id=data.get('transaction_id')
        )
        return JsonResponse({'message': 'Payment added successfully', 'id': payment.payment_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def get_payments(request):
    payments = list(Payment.objects.values())
    return JsonResponse(payments, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_payment(request, id):
    data = parse_json(request)
    try:
        payment = Payment.objects.get(payment_id=id)
        for key, value in data.items():
            setattr(payment, key, value)
        payment.save()
        return JsonResponse({'message': 'Payment updated successfully'})
    except Payment.DoesNotExist:
        return JsonResponse({'error': 'Payment not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_payment(request, id):
    try:
        payment = Payment.objects.get(payment_id=id)
        payment.delete()
        return JsonResponse({'message': 'Payment deleted successfully'})
    except Payment.DoesNotExist:
        return JsonResponse({'error': 'Payment not found'}, status=404)

# ==========================================
# AUTHENTICATION API
# ==========================================
@csrf_exempt
@require_http_methods(["POST"])
def login_passenger(request):
    data = parse_json(request)
    email = data.get('email')
    password = data.get('password')
    try:
        passenger = Passenger.objects.get(email=email, password=password)
        return JsonResponse({'message': 'Login successful', 'passenger_id': passenger.passenger_id, 'full_name': passenger.full_name})
    except Passenger.DoesNotExist:
        return JsonResponse({'error': 'Invalid email or password'}, status=401)
