from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.properties import ObjectProperty, ListProperty
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

    def method1(self, inst=None, value=None):
       # Logger.info(str(self.background.texture))
        pass
        
class ButtonGrid(GridLayout):
    gamestate = ListProperty([])

    def __init__(self, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs)
        for i in range(19*19):
            self.add_cell(i)
        self.state = go.Position()
        self.intersectionlist = []

    def on_gamestate(self, instance, value):
        Logger.info('Board state: ' + str(value))
        for inter in self.intersectionlist:
            inter_colour = self.gamestate[inter.intersection_id]
            if inter_colour == go.BLACK:
                inter.stone_image.color = (1, 1, 1, 1)
                inter.stone_image.source = inter.stone_image.sourceblack
            elif inter_colour == go.WHITE:
                inter.stone_image.color = (1, 1, 1, 1)
                inter.stone_image.source = inter.stone_image.sourcewhite
            elif inter_colour == go.OPEN:
                inter.stone_image.color = (0, 0, 0, 0)

    def add_cell(self, index):
        def make_move(instance):
            try:
                self.state.move(move_pt=instance.intersection_id)
            except go.MoveError as e:
                App.get_running_app().root.ids._info_button.text = str(e)
            else:
                App.get_running_app().root.ids._info_button.text = ''
            self.gamestate = self.state.board._board_colour

        def _update_loc(inst, value):
            '''Move a child to a new new size/pos. Used by add_cell'''
            inst.cover.size = inst.size
            inst.cover.pos = inst.pos

        intersection = Intersection(intersection_id=index)
        intersection.bind(on_press=make_move)
        self.add_widget(intersection)
        try:
            self.intersectionlist.append(intersection)
        except AttributeError:
            Clock.schedule_once(lambda dt: self.intersectionlist.append(intersection))


class Intersection(Button):
    stone_image = ObjectProperty(None)

    def __init__(self, intersection_id, **kwargs):
        super().__init__(**kwargs)
        self.intersection_id = intersection_id


class StoneImage(Image):
    pass

        
class BoardImage(Image):
    pass


class GoKivyGoApp(App):
    def build(self):
        return GoKivyGo()


if __name__ == '__main__':
    GoKivyGoApp().run()