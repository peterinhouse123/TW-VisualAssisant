# -- coding: utf-8 --
from Controller import API
from Module import Websocket
from threading import Thread
import win32con
import win32gui
import os
class main():
    def __init__(self,):
        self.Ws_App = Websocket.WS(self)


        # self.UI = UI.App(image="imageUnityGirl02.png")
        print("init_done")


    def Run(self):


        print("run_websocket")
        t = Thread(target=self.Ws_App.Init_Websocket)
        t.start()
        self.Start_UI()

        # subprocess.Popen(["electron ./Node_UI"])

        print("run_Flask")
        API.Services = self
        API.app.run()
    def Start_UI(self):
        t = Thread(target=os.system,args=['electron ./Node_UI'])
        t.start()
        # os.system("electron ./Node_UI")

    def push(self,msg):
        # print(msg)
        self.Helper_Win_Show()
        print("收到推播 ：{}".format(msg))
        self.Ws_App.Send_Order_To_All("notify",msg)
        # playsound('ring.wav')
        return msg


    def Run_Test(self):
        pass

    def Helper_Win_Show(self):
        hwnd = win32gui.FindWindow(None, 'visual-helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is show".format(hwnd))
    def Helper_Win_Hind(self):
        hwnd = win32gui.FindWindow(None, 'visual-helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM , 0, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is hind".format(hwnd))



if __name__ == '__main__':
    print("start")
    obj = main()
    obj.Run()
    # obj.Run_Test()