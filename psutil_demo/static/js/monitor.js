// 建立连接
socket = new WebSocket('ws://127.0.0.1:8000/monitor/cpu/');  // 匹配routings中的路由

// socket.onopen
socket.onopen = function () {
    var tag1 = $('<div>');
    tag1.text("连接建立成功");
    $('#conn').append(tag1);
};


function updata_uri(res) {
    var data = res.data;
    var option_per = new Array(option_per0, option_per1, option_per2, option_per3);
    var chart_per = new Array(chart_per0, chart_per1, chart_per2, chart_per3);

    data = JSON.parse(data);  // json to object

    // 水球图数据实时更新
    option_cpu_avg.series[0].data[0] = (data['cpu']['percent_avg'] / 100).toFixed(4);
    option_cpu_avg.title[0].text = 'cpu平均使用率' + '\n' + data['dt'];
    chart_cpu_avg.setOption(option_cpu_avg);   // update option_cpu_avg to chart_cpu_avg

    // 仪表盘数据实时更新
    for (var i = 0; i <= 3; i++) {
        option_per[i].series[0].data[0].value = data['cpu']['percent_per'][i];
        option_per[i].title[0].text = 'cpu' + i + '使用率' + '\n' + data['dt'];
        chart_per[i].setOption(option_per[i]);
    }
}


// 收发数据
setInterval(function () {
    socket.send('我来了');
}, 500);


socket.onmessage = function (res) {
    updata_uri(res)
}


// 断开连接
socket.onclose = function () {
    var tag2 = $('<div>');
    tag2.text('断开连接');
    $('#conn').append(tag2);
};