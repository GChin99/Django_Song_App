# This is simialr to the controller file in flask 
# There could be multilple views (controller) files that need to be imported in the apps urls.py file


from django.shortcuts import render, HttpResponse, redirect  # add redirect to import statement for Response Types
from .models import Album, Song


# Returns a string onto the page
def index(request):  #funtions now need the word request as the parameter
    return HttpResponse("this is the equivalent of @app.route('/')!")

# Returns an template
def main_page(request):  #new route (step 2)
    # displaying the infomration for the database 
    context = {
        "all_the_albums": Album.objects.all() #this is the sqlite query
    }
    return render(request, "main_page.html", context)


# Redirects to another page
def create_album(request):
    if request.method =="POST":
        print(request.POST)
        new_album = Album.objects.create(album_name=request.POST['album_name'], year=request.POST['year'])
    return redirect('/main_page')

def song_form(request):
    # displaying the infomration for the database 
    context = {
        "all_the_albums": Album.objects.all() #this is the sqlite query
    }
    return render(request, "song_form.html", context)

def create_song(request):
    if request.method == "POST":
        print(request.POST)
        new_song = Song.objects.create(song_name=request.POST['song_name'], album=Album.objects.get(id=request.POST['album']))
        return redirect('/main_page')



# Here are a few examples, to demonstrate the syntax:
# def one_method(request):                # no values passed via URL
#     pass                                
# def another_method(request, my_val):	# my_val would be a number from the URL
#     pass                                # given the example above, my_val would be 23
# def yet_another(request, name):	        # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
# def one_more(request, id, color): 	# id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'


# Response Types
# def root_method(request):
#     return HttpResponse("String response from root_method")
# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})