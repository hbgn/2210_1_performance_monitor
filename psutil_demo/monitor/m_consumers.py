from channels.generic.websocket import WebsocketConsumer

class Monitor_Consum(WebsocketConsumer):
    # 建立连接
    def websocket_connect(self, message):
        print('连接已建立成功！')
        self.accept()

    # 收发消息
    def websocket_receive(self, message):
        if message.get('text') == '我来了':
            self.close()
        else:
            self.send('ok!')

    # 断开连接
    def websocket_disconnect(self, message):
        self.close()
