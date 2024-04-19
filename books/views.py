from django.http import HttpResponse

# Create your views here.

def list_books(request):
    return HttpResponse("Hello world!")