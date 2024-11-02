from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Book


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def book_details(request):
    return render(request, 'book_details.html')

def profile(request):
    return render(request, 'profile.html')

def search_results(request):
    return render(request, 'search_results.html')




# main/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Book  # Ensure you import the correct User model

def get_recommendations(user):
    # Mock recommendation logic based on user preferences
    user_preferences = user.profile.preferences  # Assuming user has a related profile with preferences
    recommended_books = Book.objects.filter(genre__in=user_preferences.genres).exclude(id__in=user.reading_history.values_list('book_id', flat=True))
    return recommended_books

@login_required
def user_dashboard(request):
    user = request.user
    recommended_books = get_recommendations(user)
    borrowed_books = user.borrowed_books.all()
    context = {
        'user': user,
        'recommended_books': recommended_books,
        'borrowed_books': borrowed_books,
    }
    return render(request, 'user_dashboard.html', context)
