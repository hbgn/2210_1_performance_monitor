// 建立连接
socket = new WebSocket('ws://127.0.0.1:8000/monitor/mem/');  // 匹配routings中的路由

// socket.onopen
socket.onopen = function () {
    var tag1 = $('<div>');
    tag1.text("连接服务器成功");
    $('#conn').append(tag1);
};


function updata_uri(res) {
    var data = res.data;
    data = JSON.parse(data);  // json to object

    // 内存仪表盘图数据实时更新 展示值
    // option_mem_total.series[0].data[0].value = (data['mem']['total']);
    // option_mem_total.title[0].text = 'mem_total' + '\n' + data['dt'];
    // chart_mem_total.setOption(option_mem_total);
    //
    // option_mem_used.series[0].data[0].value = (data['mem']['used']);
    // option_mem_used.title[0].text = 'mem_used' + '\n' + data['dt'];
    // chart_mem_used.setOption(option_mem_used);

    // 内存仪表盘图数据实时更新 展示比例
    option_mem_used.series[0].data[0].value =
        (data['mem']['used'] * 100 / data['mem']['total']).toFixed(2);
    option_mem_used.title[0].text = 'mem_used' + '\n' + data['dt'];
    chart_mem_used.setOption(option_mem_used);

}


// 收发数据
setInterval(function () {
    socket.send('我来了');
}, 500);


socket.onmessage = function (res) {
    // console.log(res);
    updata_uri(res);
};


// 断开连接
socket.onclose = function () {
    var tag2 = $('<div>');
    tag2.text('断开连接');
    $('#conn').append(tag2);
};