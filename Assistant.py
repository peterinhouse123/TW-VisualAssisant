# -- coding: utf-8 --
from Module import UI
from Controller import API
from playsound import playsound

class main():
    def __init__(self,):
        # self.UI = UI.App(image="imageUnityGirl02.png")
        print("init_done")


    def Run(self):
        print("run_ui")
        API.Services = self
        API.app.run()


    def push(self,msg):
        # print(msg)
        print("收到推播 ：{}".format(msg))

        playsound('ring.wav')
        return msg



if __name__ == '__main__':
    print("start")
    obj = main()
    obj.Run()