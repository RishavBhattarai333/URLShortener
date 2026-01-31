URLShortener
This is a backend web application built with Django that allows authenticated users to shorten long URLs and redirect users using short links.

Features
-User authentication (register, login, logout)
-Create short URLs from long URLs
-Redirect short URLs to original links
-Manage URLs per authenticated user
-Implement the option for users to set an expiration time for short URLs.

Tech Stack
-Python
-Django
-HTML / CSS
-SQLite (development)

Project Structure
URLShortener/
├── shortener/ # Django app
├── urlshortener/ # Django project settings
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Steps to create this project

1.Create virtual environment:
python -m venv venv
Windows: venv\Scripts\activate

2. Set up a new Django project and app
django-admin startproject URLShortener
cd URLShortener

python manage.py startapp shortener

mkdir -p templates/static/   #for{css,js,images}
mkdir -p templates/shortener

3. Configure urlshortener/settings.py , shortener/models.py ,

4. Running Migrations
python manage.py makemigrations
python manage.py migrate

5. create forms.py , urls.py and configure views.py in shortener folder

6. create various templates 
base.html
register.html
login.html
create.html
my_urls.html
expired.html
shortened.html

7. Configure shortener/admin.py

8. Install dependencies:
pip install -r requirements.txt

9. # Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

10. writing .gitignore file . and using git and github for publishing repository
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/RishavBhattarai333/URLShortener.git
git branch -M main  
git push -u origin main

11. Extra Features besides URL Shortening are :
Custom URLs : users can provide custom short urls as well .
Expiration Time : admin and users can provide expiration date and time for the short urls .

