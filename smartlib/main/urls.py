from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('user-dashboard/', user_dashboard, name='user-dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('staff-dashboard/', staff_dashboard, name='staff-dashboard'),
    path('search-results/', search_results, name='search-results'),
    path('book-details/', book_details, name='book-details')
]
