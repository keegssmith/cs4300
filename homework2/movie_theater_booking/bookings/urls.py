from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='home'), 
    path('movies/', views.movie_list, name='movie_list'),
    path('book-seat/<int:movie_id>/', views.seat_booking, name='book_seat'),  
    path('submit-booking/<int:movie_id>/', views.submit_booking, name='submit_booking'),
    path('accounts/login/', views.custom_login, name='login'),
    path('booking-history/', views.booking_history, name='booking_history')
]

# API endpoints
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns += router.urls
