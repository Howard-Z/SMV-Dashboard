
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

     var polyline;
     
    // function success1(geolocation) {
    //     latlngs = [geolocation.coords.latitude, geolocation.coords.longitude]
    //     // latlngs = [34.0631, -118.4469]; //This is for testing the line functionality
    //     polyline = L.polyline([latlngs], {color: 'red'}).addTo(map);
    //     // zoom the map to the polyline
    //     map.fitBounds(polyline.getBounds());
    //     chatSocket.send(JSON.stringify({
    //         lat: geolocation.coords.latitude,
    //         long: geolocation.coords.longitude,
    //       }))
    // }
    // function error(error) {
    //     alert(error.code)
    //     alert(error.message)
    // }
    // //Once websocket initialized, get position and update MQTT
    // chatSocket.addEventListener("open", () => {
    //     navigator.geolocation.getCurrentPosition(success1, error, options)
    //     /*****************
    //     GEOLOCATION FUNCTION
    //     ******************/
    //     function success(geolocation) {
    //         polyline.addLatLng([geolocation.coords.latitude, geolocation.coords.longitude]);
    //         map.fitBounds(polyline.getBounds()); //zoom to fit
    //         chatSocket.send(JSON.stringify({
    //             lat: geolocation.coords.latitude,
    //             long: geolocation.coords.longitude,
    //         }))
    //     }
    //     navigator.geolocation.watchPosition(success, error, options)
    // })
/*****************
WEBSOCKET FUNCTION
******************/
//NEW: WebSocket
let chatSocket = 0;
if (window.location.protocol == "https:") {
    chatSocket = new WebSocket(
        'wss://'
        + window.location.host
        + '/ws/teamview'
    );
} else {
    chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/teamview'
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
        case 'daq.location':
            console.log(data['content'])
            coords = [data['content'].lat, data['content'].long]
            console.log(coords)
            if (polyline) {
                polyline.addLatLng([data['content'].lat, data['content'].long])
                map.fitBounds(polyline.getBounds());
            } else {
                var polyline = L.polyline([coords], {color: 'red'}).addTo(map);
                map.fitBounds(polyline.getBounds());
                
            }
        //TODO: implement rest of the cases for all dashboard modules
        default:
            break;

    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

})


