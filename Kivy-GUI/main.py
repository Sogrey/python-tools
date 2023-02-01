# Kivy 跨平台GUI库，源码地址： https://gitee.com/yunptop/LearnKivy2021
# pip3 install kivy
# pip3 install pillow

# ImportError: DLL load failed while importing _window_sdl2: 找不到指定的模块。应该还有些环境依赖没装，到网上找了一条命令：pip install --upgrade docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer -i https://pypi.mirrors.ustc.edu.cn/simple/ 作者：学的很杂的一个人 https://www.bilibili.com/read/cv7641679/ 出处：bilibili

import numpy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.size = (550, 400)

class MyApp(App):
    def build(self):
        return Builder.load_string("""
BoxLayout:
    orientation: "vertical"
    Button:
        text: "Button 1"
        on_press: app.btn_clicked()
    Button:
        text: "Button 2"
        """)

    def btn_clicked(self):
        print("Clicked")



# class LoginScreen(GridLayout):
#     def __init__(self,**kwargs):
#         super(LoginScreen,self).__init__(**kwargs)
#         self.cdls = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='Password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)

# class My1App(App):
#     def build(self):
#         return LoginScreen()
        
if __name__ == '__main__':
    MyApp().run()

