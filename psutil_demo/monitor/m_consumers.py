import json
from channels.generic.websocket import WebsocketConsumer
from .tools.monitor_info import Monitor

client_con = set()


class Monitor_Consum(WebsocketConsumer):
    # 建立连接
    def websocket_connect(self, message):
        print('连接已建立成功！')
        client_con.add(self)
        self.accept()

    # 收发消息
    def websocket_receive(self, message):
        m = Monitor()
        data = dict()
        if message.get('text') == '我来了':
            # 需要向前端传递监控的数据(cpu,mem,storage...)
            data = dict(
                cpu=m.cpu(),
                mem=m.mem(),
                net=m.net(),
                dt=m.dt()
            )

            """
            # self实例只会向一个客户端返回数据, 通过遍历元祖实例返回给每个客户端
            # data数据给前端需要实例化需转换为json
            """
            # print('实时采集到的数据是：',json.dumps(data))
            for info in client_con:
                info.send(json.dumps(data))

        else:
            self.send('ok!')

    # 断开连接
    def websocket_disconnect(self, message):
        self.close()
