from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import go

class GoKivyGo(BoxLayout):
    pass

class Board(FloatLayout):
    background = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        try:
            self.method1()
        except AttributeError:
            Clock.schedule_once(self.method1)
        self.state = go.Position()
            
    def method1(self, inst=None, value=None):
        Logger.info(str(self.background.texture))

        
class ButtonGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs)
        for i in range(19*19):
            self.add_cell(i)
            
    def add_cell(self, index):
        def callback(instance):
            print('My button {0} is intersection {1}'.format(instance, instance.intersection_id))

        def _update_loc(inst, value):
            '''Move a child to a new new size/pos. Used by add_cell'''
            inst.cover.size = inst.size
            inst.cover.pos = inst.pos

        intersection = Intersection(intersection_id=index)
        intersection.bind(on_press=callback)
        self.add_widget(intersection)


class Intersection(Button):
    def __init__(self, intersection_id, **kwargs):
        super().__init__(**kwargs)
        self.intersection_id = intersection_id

        
class BoardImage(Image):
    pass

class GoKivyGoApp(App):
    def build(self):
        return GoKivyGo()

if __name__ == '__main__':
    GoKivyGoApp().run()