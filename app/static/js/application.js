var markersObject = {};
var category;
var clickedMarkers = [];
var neighborhood;
var markersSelected = [];
var markersData = [];
var categoryList = [];
var neighborhoodList = [];
var curCategory = '';
var markerObj = {};
var allMarkers = [];
var Lat = 37.766396;
var Lng = -122.452927;
var zoom = 13;
// Trying out new way to draw the map and markers:
function getDynamicMap() {
    var center = new google.maps.LatLng(Lat,Lng);
    var mapOptions = {
        zoom: zoom,
        center: center,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        panControl: false,
        mapTypeControlOptions: {
            position: google.maps.ControlPosition.TOP_RIGHT
        },
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE,
            position: google.maps.ControlPosition.TOP_RIGHT
            }
    };
    map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
    buildMarkers(markersJson);
}

function buildMarkers(markersData) {
    for (var i in markersData) {
        // CHECK IF CATEGORY IS IN MASTER CATEGORY LIST
        var category = markersData[i].fields.category;
        if ($.inArray(category,categoryList)===-1) {
            categoryList.push(category);
            markersObject[category] = [];
        }
        var neighborhood = markersData[i].fields.neighborhood;
        if ($.inArray(neighborhood,neighborhoodList)===-1) {
            neighborhoodList.push(neighborhood);
            markersObject[neighborhood] = [];
        }
        // THIS MARKER OBJECT
        var markerObj = {
            id: markersData[i].pk
        }
        // COPY MARKER DATA FROM SERIALIZED JSON FIELDS
        for (var j in markersData[i].fields) {
            markerObj[j] = markersData[i].fields[j];
        }
        // ADDITIONAL MARKER SETUP

        markerObj.customInfo = '<a href="/lookup/'+markerObj.id+'">'+markerObj.category+'</a>';
        markerObj.infoWindow = new google.maps.InfoWindow({
            content: markerObj.customInfo
        });
        markerObj.marker = new google.maps.Marker({
            position: new google.maps.LatLng(markerObj.latitude,markerObj.longitude),
            map: map,
            title: markerObj.customInfo,
            category: markerObj.category
           });
        google.maps.event.addListener(markerObj.marker, 'click', function() {
            console.log(this.title);
            markerObj.infoWindow.setContent(this.title);
            markerObj.infoWindow.open(map,this);
        });

        // GET MAP CENTER AND ZOOM
        var bound = new google.maps.LatLngBounds();
        for (i = 0; i < allMarkers.length - 10; i++) {
            bound.extend( new google.maps.LatLng(allMarkers[i].latitude,allMarkers[i].longitude));
        }
        // PUSH MARKERS DATA TO ARRAYS
        markersObject[category].push(markerObj);
        markersObject[neighborhood].push(markerObj);
        allMarkers.push(markerObj);
    }
    var l = bound.getCenter();
}
/*
        function updateCategoryMarker(category,visibleFlag) {
            console.log(category + ' ' + visibleFlag);
            for(i in markersObject[category]) {
                markersObject[category][i].marker.setVisible(visibleFlag);
            }
        }

        function updateNeighborhoodMarker(neighborhood,visibleFlag) {
            console.log(neighborhood + '' + visibleFlag);
            for(i in markersObject[neighborhood]) {
                markersObject[neighborhood][i].marker.setVisible(visibleFlag);
            }
        }
*/

//Determines which function to show markers
function showMarkers() {
    if (category && !neighborhood) {
        selectCategory(category);
    } else if (neighborhood && !category) {
        selectNeighorhood(neighborhood);
    } else {
        selectNeighborhoodCategory(neighborhood, category);
    }
    hideShowButton()
}
//Shows just category
function selectCategory(category){
    for (var i in allMarkers) {
        allMarkers[i].marker.setVisible(false);
    }
    clickedMarkers = _.where(allMarkers, {category:category});
    for (j in clickedMarkers) {
        clickedMarkers[j].marker.setVisible(true);
    }
}
//Shows just neighborhood
function selectNeighorhood(neighborhood) {
    for (var i in allMarkers) {
        allMarkers[i].marker.setVisible(false);
    }
    clickedMarkers = _.where(allMarkers, {neighborhood:neighborhood});
    for (j in clickedMarkers) {
        clickedMarkers[j].marker.setVisible(true);
    }
}
//Shows both category and neighborhood
function selectNeighborhoodCategory(neighborhood, category) {
    for (var i in allMarkers) {
        allMarkers[i].marker.setVisible(false);
    }
    clickedMarkers = _.where(allMarkers, {neighborhood:neighborhood, category:category});
    for (j in clickedMarkers) {
        clickedMarkers[ j].marker.setVisible(true);
    }
}
//Selects either category or neighborhood or starts over
$(document).ready(function() {
    $('span.category').on('click',function() {
        category = $(this).attr("name");
        $('li span.category').removeClass("clicked");
        $(this).addClass("clicked");
        showMarkers();
    })
    $('span.neighborhood').on('click',function() {
        neighborhood = $(this).attr("name");
        $('li span.neighborhood').removeClass("clicked");
        $(this).addClass("clicked");
        showMarkers();
    })
    $('#clearButton').on('click',function() {
        $('li span.neighborhood').removeClass("clicked");
        $('li span.category').removeClass("clicked");
        category = '';
        neighborhood = '';
        $("#clearButton").hide();
        for (var i in allMarkers) {
            allMarkers[i].marker.setVisible(true);
        }
    });
});

//Hides/Shows clear button
function hideShowButton() {
    if (category || neighborhood) {
        $("#clearButton").show();
    }
    else {
        $("#clearButton").hide();
    }
}
//Starts with clearButton hidden:
$(document).ready(function () {
    $("#clearButton").hide();
});

google.maps.event.addDomListener(window, 'load', getDynamicMap);

//Code from original template. Currently not used. 
$(document).ready(function () {
    "use strict";
    $('#link_open').on('click', function () {
        if ($('#link_open').hasClass("clooses")) {
            $("#open_span").removeClass("close_span").addClass("open_span");
            $("#profile").removeClass("profile_closed");
            $("#link_open").removeClass("clooses");
            $("#cont").addClass("none");
        }
        else {
            $("#open_span").addClass("close_span").removeClass("open_span");
            $("#profile").addClass("profile_closed");
            $("#link_open").addClass("clooses");
            $("#cont").removeClass("none");
        }
    });
    $('#map_open').on('click', function () {
        "use strict";
        $("#cont").addClass("none");
        $("#Show_cont").removeClass("none");
    });
    $('#Show_cont').on('click', function () {
        "use strict";
        $("#cont").removeClass("none");
    });
});
