from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def main_page(request):
    return render(request, "main_page.html")

def create_album(request):
    if request.method =="POST":
        print(request.POST)
    return redirect('/main_page')