
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is my first Django web page!")

# Create your views here.
