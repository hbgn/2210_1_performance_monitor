// 建立连接
    socket = new WebSocket('ws://127.0.0.1:8000/monitor/cpu/');  // 匹配routings中的路由

    // socket.onopen
    socket.onopen = function () {
      var tag1 = $('<div>');
      tag1.text("连接建立成功");
      $('#conn').append(tag1);
    };

// 收发数据
    setInterval(function () {
        socket.send('我来了')
    },500);


// 断开连接
    socket.onclose = function () {
      var tag2 = $('<div>');
      tag2.text('断开连接');
      $('#conn').append(tag2);
    };