var map = L.map('map', {
center: [34.0699, -118.4438], //set to UCLA
zoom: 15
});
//do not modify tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
//marker test: diddy riese
var marker = L.marker([34.0631, -118.4469]).addTo(map);
// create a red polyline from an array of LatLng points. ref https://leafletjs.com/reference.html#polyline
    // async refresh speed every 0.5 second
latlngs = [34.0631, -118.4469];
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);

// zoom the map to the polyline
map.fitBounds(polyline.getBounds());

function refresh() {
    fetch('/ajax_location')
    .then(response => response.json())
    .then(result => {
        polyline.addLatLng(L.latLng(result['lat'], result['long']));
})}



//NEW: WebSocket
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/team_dash'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    switch (data['module']) {
        case 'daq.speed':
            //Speed Data
            kmh = data['content']
            screenUpdate()
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
