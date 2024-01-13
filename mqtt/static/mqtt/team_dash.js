/*****************
MAP FUNCTION
******************/
document.addEventListener('DOMContentLoaded', () => {

    //Intialize Map
    var map = L.map('map', {
        center: [34.0699, -118.4438], //set to UCLA
        zoom: 15
    });

    //OSM Map tiles
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    //Get Current Location to intialize line
    navigator.geolocation.getCurrentPosition(success1)
    var polyline;
    function success1(geolocation) {
        latlngs = [geolocation.coords.latitude, geolocation.coords.longitude]
        // latlngs = [34.0631, -118.4469]; //This is for testing the line functionality
        polyline = L.polyline([latlngs], {color: 'red'}).addTo(map);
    
        // zoom the map to the polyline
        map.fitBounds(polyline.getBounds());
    }


    /*****************
    GEOLOCATION FUNCTION
    ******************/
    function success(geolocation) {
        polyline.addLatLng([geolocation.coords.latitude, geolocation.coords.longitude]);
        map.fitBounds(polyline.getBounds()); //zoom to fit
        //ADD: push location back up to Django, confirm
    }
    navigator.geolocation.watchPosition(success)

})


/*****************
WEBSOCKET FUNCTION
******************/
//NEW: WebSocket
let chatSocket = 0;
if (window.location.protocol == "https:") {
    chatSocket = new WebSocket(
        'wss://'
        + window.location.host
        + '/ws/dashboard'
    );
} else {
    chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/dashboard'
    );
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    switch (data['module']) {
        case 'daq.speed':
            //Speed Data
            x_time.push(Date().getTime());
            y_time.push(data['content'])
            break;
        case 'power_control.energy':
            //Battery Data
            battery_update(data['content'])
            break;
        //implement rest of the cases for all dashboard modules
        default:
            break;

    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
