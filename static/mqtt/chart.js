//defining chart myChart, init empty
const ctx = document.getElementById('myChart');
let chart = new Chart(ctx, {
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

//add data to chart with label(x) and newData(y)
function addData(chart, label, newData) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(newData);
    });
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
    switch (data['module']) {
        case 'daq.speed':
            date = new Date()
            //Speed Data
            addData(chart, date.getTime(), data['content'])
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
