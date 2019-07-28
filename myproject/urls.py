"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.firstpage, name='firstpage'),
    path('home/', myapp.views.home, name='home'),
    path('signup/', myapp.views.signup, name='signup'),
    path('login/', myapp.views.login, name='login'),
    path('logout/', myapp.views.logout, name='logout'),
    path('search/', myapp.views.search, name='search'),
    path('createPost/', myapp.views.createPost, name='createPost'),
    path('delete/<str:postTitle>', myapp.views.delete, name='delete'),
]
