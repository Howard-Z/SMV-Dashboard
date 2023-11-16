// kmh gauge script
var basegradient = "repeating-conic-gradient(from 270deg, black  0deg 0.3deg, var(--color) 0.7deg 1.3deg, black  1.7deg 2deg)"

var kmh = 0;
kmh = Math.max(0, Math.min(kmh, 270));

//log styles
var green = "color: seagreen; background-color: black; border: 1px solid seagreen; padding: 4px;";
var blue = "color: darkcyan; background-color: black; border: 1px solid darkcyan; padding: 4px;";
var orange = "color: orange; background-color: black; border: 1px solid orange; padding: 4px;";
var red = "color: red; background-color: black; border: 2px solid red; padding: 3px;";

window.onload = function () {
    console.clear();
};

//initial sweep
var sweepProgress = 0;
var InitialSweepInterv = setInterval(initialSweep, 20);
function initialSweep() {
    clearInterval(InitialSweepInterv);
    //check if below is null to do things after initial sweep
    InitialSweepInterv = null;
    }


//updating the gaug each frame
var ScreenUpdateInterv = setInterval(screenUpdate, 20);
function screenUpdate() {
    //ensuring no half bars are displayed (1 bar = 2kmh)
    if (kmh % 2 == 0) {
    movescale();
    } else {
    //rounds odd speed values down. desired behavior?
    kmh--;
    movescale();
    kmh++;
    };
};



function movescale() {
    document.getElementById("gauge").style = "background: " + basegradient + ", conic-gradient(from 270deg, white 0deg " + kmh + "deg, black " + kmh + "deg);"
    document.getElementById("center_gauge").innerHTML = kmh + " kmh"
};

//switching the trip display
var km = 0;
var deci = 0;

document.getElementById("kmhslider").oninput = function () {
    if (InitialSweepInterv == null) {
    kmh = this.value;
    };
    document.getElementById("valueshow").innerHTML = kmh;
};

//NEW: WebSocket Test
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/speed'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    kmh = data['content']
    screenUpdate()
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
// async refresh speed every 0.5 second
