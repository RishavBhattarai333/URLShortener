from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import URL
from django.shortcuts import redirect

# -----------------------
# USER REGISTRATION
# -----------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create')
    else:
        form = UserCreationForm()
    return render(request, 'shortener/register.html', {'form': form})

# -----------------------
# USER LOGIN
# -----------------------
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create')
    else:
        form = AuthenticationForm()
    return render(request, 'shortener/login.html', {'form': form})

# -----------------------
# USER LOGOUT
# -----------------------
def logout_user(request):
    logout(request)
    return redirect('login')

# -----------------------
# CREATE SHORT URL
# -----------------------
@login_required(login_url="/login/")
def create_short_url(request):
    message = ""
    if request.method == "POST":
        original_url = request.POST.get('original_url')
        expires_at = request.POST.get('expires_at')  # optional expiration
        if original_url:
            url = URL.objects.create(
                user=request.user,
                original_url=original_url,
                expires_at=expires_at if expires_at else None
            )
            return render(request, 'shortener/shortened.html', {'url': url})
        else:
            message = "Please enter a valid URL."
    return render(request, 'shortener/create.html', {'message': message})

# -----------------------
# VIEW MY URLS
# -----------------------
@login_required(login_url="/login/")
def my_urls(request):
    urls = URL.objects.filter(user=request.user)
    return render(request, 'shortener/my_urls.html', {'urls': urls})

# -----------------------
# DELETE URL
# -----------------------
@login_required(login_url="/login/")
def delete_url(request, pk):
    url = get_object_or_404(URL, pk=pk, user=request.user)
    url.delete()
    return redirect('my_urls')

# -----------------------
# REDIRECT SHORT URL
# -----------------------
def redirect_short_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    
    # Check for expiration
    if url.expires_at and timezone.now() > url.expires_at:
        return render(request, 'shortener/expired.html', {'url': url})

    url.clicks += 1
    url.save()
    return redirect(url.original_url)

def home(request):
    """Redirect root URL to create URL page."""
    if request.user.is_authenticated:
        return redirect('create')
    else:
        return redirect('login')
