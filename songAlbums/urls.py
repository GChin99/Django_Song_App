"""songAlbums URL Configuration

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
# from django.contrib import admin      #this line we can comment out or just delete
from django.urls import path, include  #import include

urlpatterns = [
    # path('admin/', admin.site.urls),  #this line we can comment out or just delete
    path('', include('songApp.urls'))
]

# The urlpatterns is simply a variable that holds a list of urls that this project recognizes. Notice there are 2 arguments being passed to the url function:
# 1. a raw string representing a route pattern (in our example: '')
# 2. what to do if the pattern matches (in our example: include('app_name.urls')).  The second argument, include('app_name.urls') will resolve the rest of the route. 