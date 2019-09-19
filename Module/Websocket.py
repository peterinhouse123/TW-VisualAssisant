import json
from websocket_server import WebsocketServer
import base64


class WS():
    def __init__(self,Asseist):
        self.ws = None #type: WebsocketServer
        self.Asseist = Asseist

    def Init_Websocket(self):
        self.ws = WebsocketServer(7777, host='127.0.0.1')
        self.ws.set_fn_new_client(self.new_client)
        self.ws.set_fn_message_received(self.on_message)
        self.ws.run_forever()

    def new_client(self,ws,server):
        print("有人加入了websocket")

    def on_message(self,ws,client,data):
        print(client)
        print(data)

        #通訊協定 json格式  {'order':自定指令 ,'detail':發送的內容}

        try :
            data = base64.b64decode(data).decode()
            print(data)
            cmd = json.loads(data)
            if cmd['order'] == "push_msg":
                self.Send_Order_To_All(order="notify",detail=cmd['detail'])
            if cmd['order'] == "close_win":
                self.Asseist.Helper_Win_Hind()
        except Exception as e:
            print("Websocket 接收訊息錯誤格式")
            print(e)

    def Send_Order_To_All(self,order,detail):
        pack = {'order': order, 'detail': detail}
        print("ReadySend:{}".format(pack))
        pack = base64.b64encode(json.dumps(pack).encode())
        self.ws.send_message_to_all(pack)

if __name__ == '__main__':
    obj = WS()
    obj.Init_Websocket()