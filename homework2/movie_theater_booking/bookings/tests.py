from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
from datetime import timedelta

# Unit Tests
class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date="2025-01-01",
            duration=timedelta(hours=1, minutes=30)  # Use timedelta for duration
        )

    def test_movie_creation(self):
        self.assertTrue(isinstance(self.movie, Movie))
        self.assertEqual(self.movie.__str__(), self.movie.title)

class SeatModelTest(TestCase):

    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )

    def test_seat_creation(self):
        self.assertTrue(isinstance(self.seat, Seat))
        self.assertEqual(self.seat.__str__(), self.seat.seat_number)

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date="2025-01-01",
            duration=timedelta(hours=1, minutes=30)  # Use timedelta for duration
        )
        self.seat = Seat.objects.create(seat_number="A1", booking_status=False)
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    def test_booking_creation(self):
        self.assertTrue(isinstance(self.booking, Booking))
        self.assertEqual(self.booking.__str__(), f"{self.booking.user.username} - {self.booking.movie.title} - {self.booking.seat.seat_number}")

# Integration Tests
class MovieAPITestCase(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date="2025-01-01",
            duration=timedelta(hours=1, minutes=30)  # Use timedelta for duration
        )

    def test_movie_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_detail(self):
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookingAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date="2025-01-01",
            duration=timedelta(hours=1, minutes=30)  # Use timedelta for duration
        )
        self.seat = Seat.objects.create(seat_number="A1", booking_status=False)
        self.client.login(username='testuser', password='testpassword')
        self.booking_data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

    def test_create_booking(self):
        response = self.client.post('/api/bookings/', self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booking_list(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
