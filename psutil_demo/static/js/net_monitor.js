// 建立连接
socket = new WebSocket('ws://127.0.0.1:8000/monitor/net/');  // 匹配routings中的路由

// socket.onopen
socket.onopen = function () {
    var tag1 = $('<div>');
    tag1.text("连接服务器成功");
    $('#conn').append(tag1);
};


function updata_uri(res) {
    var data = res.data;
    data = JSON.parse(data);

    var net_T = "";

    net_T += '<thead class="layui-font-16 layui-bg-orange"><tr>';
    net_T += '<td>网卡名称</td>';
    net_T += '<td>bytes_sent</td>';
    net_T += '<td>bytes_recv</td>';
    net_T += '<td>packets_sent</td>';
    net_T += '<td>packets_recv</td>';
    net_T += '<td>address</td>';
    net_T += '<td>netmask</td>';
    net_T += '<td>broadcast</td></thead>';

    $.each(data['net'], function (index, val) {
        net_T += '<tr><td>' + val['name'] + '</td>';
        net_T += '<td>' + val['bytes_sent'] + '</td>';
        net_T += '<td>' + val['bytes_recv'] + '</td>';
        net_T += '<td>' + val['packets_sent'] + '</td>';
        net_T += '<td>' + val['packets_recv'] + '</td>';
        net_T += '<td>' + val['addr'] + '</td>';
        net_T += '<td>' + val['netmask'] + '</td>';
        if (val['broadcast']) {
            net_T += '<td>' + val['broadcast'] + '</td>';
        } else {
            net_T += '<td>无数据</td>';
        }
    });

    document.getElementById('net_table').innerHTML = net_T;


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