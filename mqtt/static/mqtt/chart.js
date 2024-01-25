//defining chart daq.speed, init empty
let daqSpeed = new Chart(document.getElementById('daq.speed'), {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Speed of Car',
        data: [],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          title: {
            display: true,
            text: "Speed (mph)",
          },
          beginAtZero: true
        },
        x: {
            title: {
              display: true,
              text: "Time (Epoch)",
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
            text: "RPM",
          },
          beginAtZero: true
        },
        x: {
            title: {
              display: true,
              text: "Time (Epoch)",
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
        //implement rest of the cases for all dashboard modules
        default:
            break;

    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
