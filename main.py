from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class GoKivyGo(BoxLayout):
    pass

class Board(FloatLayout):
    background = ObjectProperty(None)
    
    def __init__(self, **kw):
        super(Board, self).__init__(**kw)
        try:
            self.method1()
        except AttributeError:
            Clock.schedule_once(self.method1)
            
    def method1(self, inst=None, value=None):
        Logger.info(str(self.background.texture))

        
class ButtonGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs)
        for i in range(19*19):
            self.add_cell(i)
            
    def add_cell(self, index):
        def _update_loc(inst, value):
            '''Move a child to a new new size/pos. Used by add_cell'''
            inst.cover.size = inst.size
            inst.cover.pos = inst.pos

        b = Button(text=str(index))
        ##self.bind(pos=_update_loc, size=_update_loc)
        self.add_widget(b)

        
class BoardImage(Image):
    pass

class GoKivyGoApp(App):
    def build(self):
        return GoKivyGo()

if __name__ == '__main__':
    GoKivyGoApp().run()