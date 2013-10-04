from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from app.models import Complaints, Comments
from django.shortcuts import render, redirect, render_to_response
from app.forms import SigninForm, SignupConfirmForm, CommentsForm, LookupForm, SubmitForm
from django.contrib.auth.models import User
import requests, datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.core import serializers
from django import forms

# Function for new users to sign up:
def signup(request):
    print 'SIGNUP!!!!!!!!!!!!!!!!!'
    print request.session['currentUrl']
    if request.method == "POST" and 'buttonform1' in request.POST:
        form = SignupConfirmForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            thisUser = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if thisUser is not None and thisUser.is_active:
            auth.login(request, thisUser)
            return HttpResponseRedirect(request.session['currentUrl'])
    elif request.method == "POST" and 'buttonform2' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(request.session['currentUrl'])
            else:
                return HttpResponse("Your username and password do not match.")
    else:
        form1 = SignupConfirmForm()
        form2 = SigninForm()
        data = {
            'form1': form1,
            'form2': form2,
        }
        return render(request, 'signup.html', data)

#Let a user sign in:
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("return_url")
        else:
            return HttpResponse("Your username and password do not match.")
    else:
        form = SigninForm()
        return render(request, 'signup.html', {'form':form})

#Let a user sign out:
def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/')

# Get all case reports:
def reports(request):
#    payload = {'category':'category', 'neighborhood':'neighborhood'}
    r = requests.get('http://data.sfgov.org/resource/vw6y-z8j6.json')
#    print r.status_code
    cases = r.json()
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
            Complaints.objects.get_or_create(category=category, case_id=case_id, status = status, neighborhood = neighborhood,
                supervisor_district = supervisor_district, longitude=longitude, latitude=latitude, opened=opened,
                updated=updated, address=address, request_details=request_details)
        except KeyError:
            print 'You have a KeyError'
            i = i + 1
    return HttpResponse("Database updated")


def about(request):
    return HttpResponse("citizen311 about")

#Complaint submit function:
def submit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/signup')
    if request.method == "POST":
        form = SubmitForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            category=form.cleaned_data['category']
            comments=form.cleaned_data['comments']
            total_id = Complaints.objects.count()
            print total_id
            print address
            new_id = total_id + 1
            string_id = str(new_id)
            case_id = "citizen311_"+string_id
            print case_id
            comments_created_date=datetime.datetime.now()
            user_id = request.user.id
            Complaints.objects.create(address=address,
                                      category=category,
                                      case_id=case_id,
                                      id=new_id,
                                      latitude=latitude,
                                      longitude=longitude)
            Comments.objects.create(comments=comments,
                                    comments_created_date=comments_created_date,
                                    user_id=user_id,
                                    complaints_id=new_id)
        return HttpResponseRedirect('/')

    else:
        form = SubmitForm()
        data = {
            "form":form
        }
        return render(request, 'submit.html', data)



#Complaint look up function:
def lookup(request):
    if request.method == "POST":
        form = LookupForm(request.POST)
        if form.is_valid():
            case_id=form.cleaned_data['case_id']
            complaint = Complaints.objects.get(case_id=case_id)
            id = complaint.id
            complaint = Complaints.objects.get(pk=id)
            data = {
                "complaint":complaint
            }
            print data
            return render(request, 'lookup.html', data)
    else:
        form = LookupForm()
        data = {
            "form":form
        }
        return render(request, 'lookup.html', data)

#User sends a comment:
"""
def comments(request):
    if not request.user.is_authenticated():
        return HttpResponse("You need to be signed in first.")
    else:
        if request.method == "POST":
            form = CommentsForm(request.POST)
            if form.is_valid():
                print "form is valid"
                url = HttpRequest.get_full_path()
                print url
                user_id = request.user.id
                complaint_id = form.cleaned_data['complaints']
                comments = form.cleaned_data['comments']
                ThisComment = Comments(user_id=user_id, comments=comments, complaints_id=complaint_id)
#                ThisComment = Comments(user=request.user, complaints=complaint, comments=comments)
                ThisComment.save()
            return HttpResponse(request, url)
        else:
            form = CommentsForm()
            data = {
                "form":form
            }
            return render(request, 'comments.html', data)
"""

#Get all data for map markers:
def markers_info(request):
    all_info = list(Complaints.objects.all()) + list(Comments.objects.all())
    user_info = User.objects.select_related().only('username', 'id')
#    user_info = serializers.serialize('json', user_info)
    json = serializers.serialize('json', all_info)
    print 'user_info_____________________'
    print user_info[0].email
#    assert isinstance(user_dict, object)
    return render(request, 'markers-info.html', { 'json': json })

def lookup_report(request, id):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            complaint = Complaints.objects.get(id=id)
            print "form is valid"
            user_id = request.user.id
            complaint_id = complaint.id
            comments = form.cleaned_data['comments']
            ThisComment = Comments(user_id=user_id, comments=comments, complaints_id=complaint_id)
    #                ThisComment = Comments(user=request.user, complaints=complaint, comments=comments)
            ThisComment.save()
        complaint = Complaints.objects.get(id=id)
        form = CommentsForm()
        data = {
            'complaint': complaint,
            'form': form,
        }
        return render(request, "lookup.html", data)
    else:
        currentUrl = request.get_full_path()
        request.session['currentUrl'] = currentUrl
        print request.session['currentUrl']
        complaint = Complaints.objects.get(id=id)
        form = CommentsForm()
        data = {
            'complaint': complaint,
            'form': form,
        }
        return render(request, "lookup.html", data)










