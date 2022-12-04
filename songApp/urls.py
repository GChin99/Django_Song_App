# URLs holds all of the routes 

from django.urls import path
#this imports the views file.  (if we have multiple views/controller files, we would need to add  them to this import)
# the . indicates that the views file can be found in the same directory as this file
from . import views

# This is the same url function, but this time our arguments indicate that:
# '' - the rest of the route both starts and ends with nothing (i.e. "/" is the full route), and
# views.index - if the requested route matches this pattern, then the function with the name "index" from this app's views.py file will be invoked.
urlpatterns = [
    path('', views.index),
    path('main_page', views.main_page),
    path('create/album', views.create_album),
]


# Here are a few examples, to demonstrate the syntax:
# urlpatterns = [
#         path('bears', views.one_method),                        # would only match localhost:8000/bears
#         path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
#         path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
#         path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
# ]


# Response Types
# In Django, there are many different ways we can return a response.  We will look into returning a HTML template in the next lesson, for now let's focus on these.
    # HttpResponse: Can be used to pass a string as a response.
    # Redirect: Used to navigate to a different view method, before a final response is sent to the client. ***Note*** Even though we don't include the first / in our project urls.py file, when redirecting, you should provide the whole path, starting with the first /.
    # JsonResponse: Used to return a JSON object

# urlpatterns = [
#     path('', views.root_method),
#     path('another_route', views.another_method),
#     path('redirected_route', views.redirected_method
# ]