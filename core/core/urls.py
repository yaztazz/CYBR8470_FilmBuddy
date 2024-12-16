"""Movierec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),           # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register, name='register'),  # Register page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('watch-history/', views.watch_history, name='watch_history'),
    path('top-rated/', views.top_rated, name='top_rated'),
    path('recommend-movie/', views.recommend_movie, name='recommend_movie'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('review-history/', views.review_history, name='review_history'),
    path('g-rated/', views.g_rated, name='g_rated'),
    path('pg-rated/', views.pg_rated, name='pg_rated'),
    path('pg13-rated/', views.pg13_rated, name='pg13_rated'),
    path('approve-reviews/', views.approve_reviews, name='approve_reviews'),
    path('manage-users/', views.manage_users, name='manage_users'),
]
   

