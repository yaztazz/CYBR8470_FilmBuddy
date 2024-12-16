##Imported code- geeksforgeeks.org


from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Emenitites, Movie
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def home(request):
    emenities = Emenitites.objects.all()
    context = {'emenities': emenities}
    return render(request, 'home.html', context)

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()
        social_media = request.POST.get('social_media', '').strip()
        two_factor = request.POST.get('two_factor', '').strip()

        # Ensure all fields are filled
        if not all([username, email, password, password2, social_media, two_factor]):
            messages.error(request, 'Please fill out all fields.')
        elif password != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            # Create the user
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page

    return render(request, 'register.html')

@login_required(login_url="/login/")
def api_movies(request):
    movies_objs = Movie.objects.all()
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = [int(e) for e in emenities.split(',') if e.isdigit()]
        movies_objs = movies_objs.filter(emenities__in=emenities).distinct()
    
    payload = [{'movie_name': movie_obj.movie_name,
                'movie_description': movie_obj.movie_description,
                'movie_image': movie_obj.movie_image,
                'price': movie_obj.price} for movie_obj in movies_objs]
    
    return JsonResponse(payload, safe=False)

def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            
            user_obj = authenticate(username=username, password=password)
            
            if user_obj:
                login(request, user_obj)
                return redirect('/')
            
            messages.error(request, "Wrong Password")
            return redirect('/login/')
            
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
        
    return render(request, "login.html")

def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            
            messages.success(request, "Account created")
            return redirect('/login/')
        
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    
    return render(request, "register.html")

def custom_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from .models import Movie  # Ensure Movie model is imported

def dashboard(request):
    if request.user.is_authenticated:
        # Get user group
        group = request.user.groups.first()  # Assumes a user belongs to one group
        group_name = group.name if group else "No Group"  # Fallback if no group exists

        # Fetch movies from the database
        movies = Movie.objects.all()  # Query the Movie model

        # Context passed to the template
        context = {
            'movies': movies,
            'group_name': group_name,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login')  # Redirect unauthenticated users to the login page


def is_admin(user):
    return user.groups.filter(name="Admin").exists()


@login_required
@user_passes_test(is_admin)
def approve_reviews(request):
    # Placeholder: Implement logic to display and approve reviews
    return render(request, 'approve_reviews.html')



def manage_users(request):
    # Placeholder: Implement logic to manage users
    return render(request, 'manage_users.html')

def watch_history(request):
    return render(request, 'watch_history.html')

def top_rated(request):
    return render(request, 'top_rated.html')

def recommend_movie(request):
    return render(request, 'recommend_movie.html')

def submit_review(request):
    return render(request, 'submit_review.html')

def review_history(request):
    return render(request, 'review_history.html')

def g_rated(request):
    return render(request, 'g_rated.html', {'group_name': "Teacher"})

def pg_rated(request):
    return render(request, 'pg_rated.html', {'group_name': "Teacher"})

def pg13_rated(request):
    return render(request, 'pg13_rated.html', {'group_name': "Teacher"})



def logout_view(request):
    logout(request)
    return redirect('login')

