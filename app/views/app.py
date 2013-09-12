from django.http import HttpResponse

def get_JSON(request):
    url = 'http://data.sfgov.org/resource/vw6y-z8j6.json'

def signup(request):
    return HttpResponse("citizen311 signup")

def reports(request):
    return HttpResponse("citizen311 reports")

def about(request):
    return HttpResponse("citizen311 about")

def submit(request):
    return HttpResponse("citizen311 submit")