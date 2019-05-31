from django.http import HttpReponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs) :
	print(args, kwargs)
	print(request.user)

	return render(request, "home.html", {})
	def contact_view(request, *args, **kwargs):
		return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def social view(request, *args, **kwags):
    return HttpReponse("<h1>Social Page</h1>")
