





from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', include('posts.urls')),
]






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'posts',   
]

AUTH_USER_MODEL = 'accounts.CustomUser'
