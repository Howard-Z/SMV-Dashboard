var Interval;
/**************************************
TIMER FUNCTION: runs timer at top of page
***************************************/
function timer_s(seconds, minutes, hours)
{
  console.log(seconds)
  console.log(minutes)
  console.log(hours)

  var p2 = minutes; 
  var p1 = seconds; 
  var p3 = hours;
  var appendTens = document.getElementById("tens")
  var appendSeconds = document.getElementById("seconds")
  var appendHours = document.getElementById("hours")
  
  if (p1){
    if (p1 < 9) appendTens.innerHTML = "0" + p1;
    else appendTens.innerHTML = p1;
  }
  if (p2){
    if (p2 < 9) appendSeconds.innerHTML = "0" + p2;
    else appendSeconds.innerHTML = p2;
  }
  if (p3) appendHours.innerHTML = p3;
  function startTimer () {
      p1++; 
      if(p1 <= 9){
        appendTens.innerHTML = "0" + p1;
      }
      
      if (p1 > 9){
        appendTens.innerHTML = p1;
      } 
      
      if (p1 > 59) {
        p2++;
        appendSeconds.innerHTML = "0" + p2;
        p1 = 0;
        appendTens.innerHTML = "0" + 0;
      }
              
      if (p2 > 59) {
          p3++;
          appendSeconds.innerHTML = "0" + 0;
          appendTens.innerHTML = "0" + 0;
          p1 = 0;
          p2 = 0;
          appendHours.innerHTML = "0" + p3;
        }
      if (p3 > 9) {
          appendHours.innerHTML = p3;
      }
      if (p2 > 9){
        appendSeconds.innerHTML = p2;
      }
    
    }
  Interval = setInterval(startTimer, 1000);
}
var dateTime = new Date().getTime();
var startMin = dateTime/60000;
var startSec = dateTime/1000;

//defining chart daq.speed, init empty
let daqSpeed = new Chart(document.getElementById('daq.speed'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Speed of Car',
      data: [],
      borderWidth: 1,
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Car Speed (mph)',
        color: "#adadad"
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Speed (mph)",
          color: "#c2c2c2"
        },
        beginAtZero: true
      },
      x: {
          title: {
            display: true,
            ticks: {
              beginAtZero:true,
              min: 0,
              max: 100  
            },
            text: "Time (Min:Sec)",
            color: "#c2c2c2"
          },
        }
    }
  }
});

  //defining chart rpm, init empty
let rpm = new Chart(document.getElementById('rpm'), {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Bear 1 RPM',
        data: [],
        borderWidth: 1,
        borderColor: "#FF0000",
      }, {
        label: 'Bear 2 RPM',
        data:[],
        borderWidth:1,
        borderColor: "#0000FF",
      }]
    },
    options: {
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'RPM of Motors 1 and 2'
        }
     },
      scales: {
        y: {
          title: {
            display: true,
            text: "Time (Min:Sec)",
          },
        }
    }
  }
});
var maxValues = 10;
setInterval(() => {
  var currentDateTime = new Date().getTime();
  var currentMin = Math.trunc(currentDateTime/60000-startMin);
  var currentSec = Math.trunc(currentDateTime/1000-startSec);
  if (currentSec>59){
    currentSec%=60;
  }
  var currentTime = currentMin +":"+ currentSec;

  daqSpeed.data.labels.push(currentTime);
  daqSpeed.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  if (daqSpeed.data.labels.length > maxValues) {
    daqSpeed.data.labels.shift();
    daqSpeed.data.datasets[0].data.shift();
  }

  rpm.data.labels.push(currentTime);
  rpm.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  rpm.data.datasets[1].data.push(Math.floor((Math.random() * 20) + 1));
  if (rpm.data.labels.length > maxValues) {
    rpm.data.labels.shift();
    rpm.data.datasets[0].data.shift();
    rpm.data.datasets[1].data.shift();
  }

  power.data.labels.push(currentTime);
  power.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  if (power.data.labels.length > maxValues) {
    power.data.labels.shift();
    power.data.datasets[0].data.shift();
  }

  current.data.labels.push(currentTime);
  current.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  if (current.data.labels.length > maxValues) {
    current.data.labels.shift();
    current.data.datasets[0].data.shift();
  }

  voltage.data.labels.push(currentTime);
  voltage.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  if (voltage.data.labels.length > maxValues) {
    voltage.data.labels.shift();
    voltage.data.datasets[0].data.shift();
  }

  temp.data.labels.push(currentTime);
  temp.data.datasets[0].data.push(Math.floor((Math.random() * 20) + 1));
  if (temp.data.labels.length > maxValues) {
    temp.data.labels.shift();
    temp.data.datasets[0].data.shift();
  }
  temp.update();
  voltage.update();
  current.update();
  power.update();
  rpm.update();
  daqSpeed.update();

  
}, 1000);


//defining chart daq.speed, init empty
let power = new Chart(document.getElementById('power_control.power'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Power',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Fuel Cell Power (W)'
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Fuel Cell Power (W)",
        },
        beginAtZero: true
      },
      x: {
          title: {
            display: true,
            text: "Time (Min:Sec)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let current = new Chart(document.getElementById('power_control.current'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Current',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Fuel Cell Current (A)'
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Current (A)",
        },
        beginAtZero: true
      },
      x: {
          title: {
            display: true,
            text: "Time (Min:Sec)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let voltage = new Chart(document.getElementById('power_control.voltage'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Voltage (V)',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Fuel Cell Voltage (V)'
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Voltage (V)",
        },
        beginAtZero: true
      },
      x: {
          title: {
            display: true,
            text: "Time (Min:Sec)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let temp = new Chart(document.getElementById('power_control.temperature'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Temperature (C)',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Fuel Cell Temperature (C)'
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Temperature (C)",
        },
        beginAtZero: true
      },
      x: {
          title: {
            display: true,
            text: "Time (Min:Sec)",
          },
        }
    }
  }
});

//add data to chart with label(x) and newData(y)
function addData(chart, label, newData, index=-1) {
    if (index==-1) {
      chart.data.labels.push(label);
      chart.data.datasets.forEach((dataset) => {
          dataset.data.push(newData);
      });
    }
    else {
      chart.data.labels.push(label);
      chart.data.datasets[index].data.push(newData)
    }
    chart.update('none');
}

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
    date = new Date()
    switch (data['module']) {
        case 'timing':
          //case: initial time from most recent trip
          timer_s(data['second'], data['minute'], data['hours'])
          break;
        case 'daq.speed':
            //Speed Data
            addData(daqSpeed, date.getTime(), data['content'])
            break;
        case 'bear1.rpm':
            //Motor 1 RPM data
            addData(rpm, date.getTime(), data['content'],0)
            break;
        case 'bear2.rpm':
            //Motor 1 RPM data
            addData(rpm, date.getTime(), data['content'],1)
            break;
        case 'bear2.rpm':
          //Motor 1 RPM data
          addData(rpm, date.getTime(), data['content'],1)
          break;
        case 'power_control.temperature':
          //Motor 1 RPM data
          addData(temp, date.getTime(), data['content'],0)
          break;
        case 'power_control.voltage':
          //Motor 1 RPM data
          addData(voltage, date.getTime(), data['content'],0)
          break;
        case 'power_control.current':
          //Motor 1 RPM data
          addData(current, date.getTime(), data['content'],0)
          break;
        case 'power_control.power':
          //Motor 1 RPM data
          addData(power, date.getTime(), data['content'],0)
          break;
        //implement rest of the cases for all dashboard modules
        default:
            break;

  }
};

chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};