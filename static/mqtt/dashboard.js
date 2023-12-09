//SECTION 2: HANDLING FUNCTIONS
function battery_update(battery_level) {
    indicator = document.getElementById("battery_indicator")
    indicator.style = `height:${battery_level}%`
    // added color changes based on low battery
    if (battery_level < 10) {
        console.log(10)
        indicator.setAttribute('class', "battery-level alert")
    } else if (battery_level < 20) {
        console.log(20)
        indicator.setAttribute('class', "battery-level warn")
    } 
}
//NEW: WebSocket
const chatSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/dashboard'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    switch (data['module']) {
        case 'daq.speed':
            //Speed Data
            mph = data['content']
            document.getElementById("center_gauge").innerHTML = `${mph} mph`
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
    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/dashboard'
    );
};
