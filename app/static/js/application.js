var map;
var marker;
var customInfo;
var infoWindow;

/*function bindInfoWindow(marker, map, infoWindow, customInfo) {
    google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(customInfo);
        infoWindow.open(map, marker);
    });
});*/
/*function drawComplaints() {
    for (i=0; i < json.length; i++) {
        var lat = json[i].point.latitude;
        var lng = json[i].point.longitude;
        var customInfo = json[i].category;
        var infoWindow = new google.maps.InfoWindow({
            content: customInfo
        });
        var marker = new google.maps.Marker ({
            position: new google.maps.LatLng(lat,lng),
            map: map,
            title: customInfo
        });
        google.maps.event.addListener(marker, 'click', function() {
            infoWindow.open(map,marker);
        });
        console.log('finally');
    }
}*/

/*function drawComplaints() {
    for (var id in complaints) {
        var lat = complaints[id].point.latitude;
        var lng = complaints[id].point.longitude;
        var address = complaints[id].address;
        var customInfo = complaints[id].category;
        var infoWindow = new google.maps.InfoWindow({
            content: customInfo
        });
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat,lng),
            map: map,
            title: customInfo
        });
        google.maps.event.addListener(marker, 'click', function() {
            infoWindow.open(map,marker);
        });
        console.log(address);
        //bindInfoWindow(marker, map, infoWindow, customInfo);
    }
}
//drawComplaints();


/*Start Facebook here*/

/*$(document).ready(function() {
    $('#comments').append( Mustache.render( $('#comments-template').html(), comments) );
});*/

window.fbAsyncInit = function() {
    FB.init({
        appId : '146925758848407', // App ID
        channelUrl : '//WWW.YOUR_DOMAIN.COM/channel.html', // Channel File
        status : true, // check login status
        cookie : true, // enable cookies to allow the server to access the session
        xfbml : true // parse XFBML
    });

    // Here we subscribe to the auth.authResponseChange JavaScript event. This event is fired
    // for any authentication related change, such as login, logout or session refresh. This means that
    // whenever someone who was previously logged out tries to log in again, the correct case below
    // will be handled.
    FB.Event.subscribe('auth.authResponseChange', function(response) {
        // Here we specify what we do with the response anytime this //event occurs.
        console.log(response);
        if (response.status === 'connected') {
            // The response object is returned with a status field that lets the app know the current
            // login status of the person. In this case, we're handling the situation where they
            // have logged in to the app.
            testAPI();
        } else if (response.status === 'not_authorized') {
            // In this case, the person is logged into Facebook, but not into the app, so we call
            // FB.login() to prompt them to do so.
            // In real-life usage, you wouldn't want to immediately prompt someone to login
            // like this, for two reasons:
            // (1) JavaScript created popup windows are blocked by most browsers unless they
            // result from direct interaction from people using the app (such as a mouse click)
            // (2) it is a bad experience to be continually prompted to login upon page load.
            FB.login();
        } else {
            // In this case, the person is not logged into Facebook, so we call the login()
            // function to prompt them to do so. Note that at this stage there is no indication
            // of whether they are logged into the app. If they aren't then they'll see the Login
            // dialog right after they log in to Facebook.
            // The same caveats as above apply to the FB.login() call here.
            FB.login();
        }
    });
};
(function(d){
    var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement('script'); js.id = id; js.async = true;
    js.src = "//connect.facebook.net/en_US/all.js";
    ref.parentNode.insertBefore(js, ref);
    }(document));

function testAPI() {
    console.log('Welcome! Fetching your information.... ');
    FB.api('/me', function(response) {
        console.log(response);
        console.log('Good to see you, ' + response.name + '.');
    });
}

function getDynamicMap(position) {
    var mapOptions = {
        center: new google.maps.LatLng(37.797677,-122.394339),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    console.log("complaints");
    for (var id in complaints) {
        var lat = complaints[id].point.latitude;
        var lng = complaints[id].point.longitude;
        var address = complaints[id].address;
        var customInfo = '<a href="#" onclick="fillCommentsBox('+complaints[id].case_id+')">'+complaints[id].category+'</a>';
        //var customInfo = '<a href="http://bootcamp.rocketu.com/exercises/project/reports-page.html$'+complaints[id].case_id+'">'+complaints[id].case_id+'</a>';
        var infoWindow = new google.maps.InfoWindow({
            content: customInfo
        });
        var	marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat,lng),
            map: map,
            title: customInfo
           });
        google.maps.event.addListener(marker, 'click', function() {
            console.log(this.title);
            infoWindow.setContent(this.title);
            infoWindow.open(map,this);
            console.log('click');
        });
    }
}
console.log('success');
google.maps.event.addDomListener(window, 'load', getDynamicMap);

function fillCommentsBox(case_id) {
    var commentsMustache = $('#comments-template').html();
    var commentsOutput = Mustache.render(commentsMustache, comments[case_id]);
    $('#comments').html(commentsOutput);
    var complaintsMustache = $('#complaints-template').html();
    console.log(complaints[case_id]);
    var complaintsOutput = Mustache.render(complaintsMustache, complaints[case_id]);
    $('#complaints').html(complaintsOutput);
}
/*if (window.location.href.search('case_id=')!==-1) {
var case_id = getQueryVariable('case_id');
currentComplaint = complaints[case_id];
currentComment = comments[case_id];
console.log(currentComplaint);
}*/

