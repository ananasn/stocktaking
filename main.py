import kivy
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy_garden.xcamera import XCamera

import time
from io import BytesIO
import base64
import requests
import json

ADR = 'http://de.futoke.ru'

class MyXCamera(XCamera):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def shoot(self):
        def on_success(filename):
            self.dispatch('on_picture_taken', filename)
        img = self.export_as_image()
        buff = BytesIO()
        buff.seek(0)
        img.save(buff, fmt='png')
        data = {'test': 'test_info', 'hello': 'world'}

        requests.post(ADR, json=json.dumps(data))
        on_success('test')


class MyApp(App):

    def print_str(self, item):
        print(item)



if __name__ == '__main__':
    MyApp().run()