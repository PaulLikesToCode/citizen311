from django.http import HttpResponse
from app.models import Complaints, Comments
from django.shortcuts import render
from app.forms import SigninForm, SignupConfirmForm, CommentsForm
from django.contrib.auth.models import User
import requests
from django.contrib.auth import authenticate
from django.contrib.auth import hashers

#    url = 'http://data.sfgov.org/resource/vw6y-z8j6.json'

# Function for new users to sign up:
def signup(request):
    if request.method == "POST":
        form = SignupConfirmForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return HttpResponse('Thanks for signing up.')
    else:
        form = SignupConfirmForm()
        return render(request, 'signup.html', {'form': form})

#Let a user sign in:
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return HttpResponse("Thanks for signing in.")
        else:
            return HttpResponse("Your username and password do not match.")
    else:
        form = SigninForm()
        return render(request, 'login.html', {'form':form})


def reports(request):
#    payload = {'category':'category', 'neighborhood':'neighborhood'}
    r = requests.get('http://data.sfgov.org/resource/vw6y-z8j6.json')
#    print r.url
#    print r.status_code
    cases = r.json()
#    print len(cases)
    for i in range(0, len(cases)):
        try:
            category = cases[i]['category']
            case_id = cases[i]['case_id']
            longitude = cases[i]['point']['longitude']
            latitude = cases[i]['point']['latitude']
            status = cases[i]['status']
            neighborhood = cases[i]['neighborhood']
            supervisor_district = cases[i]['supervisor_district']
            opened = cases[i]['opened']
            updated = cases[i]['updated']
            address = cases[i]['address']
            request_details = cases[i]['request_details']
            Complaints.objects.create(category=category, case_id=case_id, status = status, neighborhood = neighborhood,
                supervisor_district = supervisor_district, longitude=longitude, latitude=latitude, opened=opened,
                updated=updated, address=address, request_details=request_details)
        except KeyError:
            print 'You have a KeyError'
            i = i + 1
    return HttpResponse("Database updated")


def about(request):
    return HttpResponse("citizen311 about")

def submit(request):
    return HttpResponse("citizen311 submit")


def lookup(request, id):
    complaint = Complaints.objects.get(pk=id)
    data = {
        "complaint":complaint
    }
    print data
    return render(request, 'lookup.html', data)


'''
def lookup(request):
    return render(request, 'lookup.html')
'''

def comments(request):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            print "form is valid"
            user = form.cleaned_data['username']
            complaints = form.cleaned_data['complaints']
            comments = form.cleaned_data['comments']
            ThisComment = Comments(user_id=user, comments=comments, complaints_id=complaints)
            ThisComment.save()
            print ThisComment
        return HttpResponse("Thank you for your input.")
    else:
        form = CommentsForm()
        data = {
            "form":form
        }
        return render(request, 'comments.html', data)











