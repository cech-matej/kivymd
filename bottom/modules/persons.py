from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget

import json


'''person_list = [{"name": "Karel Nový", "state": "CZE"},
               {"name": "Ivan Hrozný", "state": "RUS"},
               {"name": "John Walker", "state": "USA"}]'''


class MyItem(TwoLineAvatarListItem):
    def __init__(self, name, invention, state, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = invention
        self.secondary_text = name
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f'images/state/{state}.png')
        self.add_widget(self.image)

    '''def on_press(self):
        print(self.text)

    def on_touch_down(self, touch):
        print(touch)
        self.image.source = 'images/blue.png'

    def on_touch_up(self, touch):
        print(touch)
        self.image.source = 'images/green.png'''


class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()

        with open('modules/person_list.json', encoding='utf8') as f:
            person_list = json.load(f)

        for person in person_list['person']:
            list.add_widget(MyItem(name=person['name'], invention=person['invention'], state=person['state']))

        scrollview.add_widget(list)
        self.add_widget(scrollview)
