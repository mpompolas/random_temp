from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import webbrowser
import requests


class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # use a (r, g, b, a) tuple
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)

        self.btn1 = Button(text='Nas!', background_color=red, font_size=50)
        self.btn1.bind(on_press=self.callback1)

        self.btn2 = Button(text='Zanos!', background_color=red, font_size=50)
        self.btn2.bind(on_press=self.callback2)

        self.label1 = (Label(text='User Name'))
        layout.add_widget(self.label1)

        self.label2 = (Label(text='User Name'))
        layout.add_widget(self.label2)

        layout.add_widget(self.btn1)
        layout.add_widget(self.btn2)

        return layout

    def open_url(self, user):

        lat = 45.514951
        lon = -73.570179
        destination_lat = [45.451862, 45.551862]
        destination_lon = [-73.872942, -73.692942]

        first = 'http://maps.google.com/?daddr='
        start = '&saddr='
        walk = '&dirflg=w'
        zoom = '&sspn=0.001,0.001'
        url = first + str(destination_lat[user]) + ',' + str(destination_lon[user]) + start + str(lat) + ',' + str(
            lon) + walk + zoom

        webbrowser.open(url)

    def callback1(self, event):
        print("button 1asfasfasfasdfsdf touched")
        print(dir(self.label1))
        self.btn1.text = "asdfdfs"
        self.label1.canvas = (0, 0, 1.5, 2.5)
        self.open_url(0)

    def callback2(self, event):
        print("button 2 touched")
        self.label2.text = "blablabalb"
        self.open_url(1)


TestApp().run()