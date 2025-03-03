from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def home(request):
    return render(request, 'bookings/base.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def submit_booking(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        user = request.user

        # Create booking
        Booking.objects.create(movie=movie, seat=seat, user=user)

        # Mark the seat as booked
        seat.booking_status = True
        seat.save()

        return redirect('booking_history')

    return redirect('book_seat', movie_id=movie_id)

def booking_history(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
