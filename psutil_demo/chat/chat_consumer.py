# 建立连接，发送数据，断开连接
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

client_con = []


class ChatConsumer(WebsocketConsumer):

    # 客户端向服务器请示请求，建立连接
    def websocket_connect(self, message):
        print("连接已建立！！！")
        self.accept()
        self.send('欢迎来到我的站点，可以开始聊天了！')
        client_con.append(self)  # 储存客户端连接

    # 建立连接 (服务器硬件开发数据通过websocket_receive发送给前端)
    def websocket_receive(self, message):
        info = message.get('text')
        # 后端收到前端消息后，执行关闭
        if info == "关闭":
            self.close()
        else:
            # 遍历每个客户端，发送信息给前端
            for cli in client_con:
                cli.send(info)
        # self.send(message['text'] + '收到')

    # 断开连接
    def websocket_disconnect(self, message):
        print('连接已断开！！！')
        # self.close()
        raise StopConsumer
