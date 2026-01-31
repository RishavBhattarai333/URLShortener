from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),  # <-- ROOT URL
    
    # User auth
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # URL management
    path('create/', views.create_short_url, name='create'),
    path('my-urls/', views.my_urls, name='my_urls'),
    path('delete/<int:pk>/', views.delete_url, name='delete'),

    # Redirect short URL
    path('<str:short_code>/', views.redirect_short_url, name='redirect'),
    
]
