from django.urls import path
from . import views

urlpatterns = [
    # Passenger
    path('api/passengers/add/', views.add_passenger, name='add_passenger'),
    path('api/passengers/', views.get_passengers, name='get_passengers'),
    path('api/passengers/update/<int:id>/', views.update_passenger, name='update_passenger'),
    path('api/passengers/delete/<int:id>/', views.delete_passenger, name='delete_passenger'),

    # Ship
    path('api/ships/add/', views.add_ship, name='add_ship'),
    path('api/ships/', views.get_ships, name='get_ships'),
    path('api/ships/update/<int:id>/', views.update_ship, name='update_ship'),
    path('api/ships/delete/<int:id>/', views.delete_ship, name='delete_ship'),

    # Schedule
    path('api/schedules/add/', views.add_schedule, name='add_schedule'),
    path('api/schedules/', views.get_schedules, name='get_schedules'),
    path('api/schedules/update/<int:id>/', views.update_schedule, name='update_schedule'),
    path('api/schedules/delete/<int:id>/', views.delete_schedule, name='delete_schedule'),

    # Booking
    path('api/bookings/add/', views.add_booking, name='add_booking'),
    path('api/bookings/', views.get_bookings, name='get_bookings'),
    path('api/bookings/update/<int:id>/', views.update_booking, name='update_booking'),
    path('api/bookings/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    # Payment
    path('api/payments/add/', views.add_payment, name='add_payment'),
    path('api/payments/', views.get_payments, name='get_payments'),
    path('api/payments/update/<int:id>/', views.update_payment, name='update_payment'),
    path('api/payments/delete/<int:id>/', views.delete_payment, name='delete_payment'),

    # Authentication
    path('api/login/', views.login_passenger, name='login_passenger'),
]
