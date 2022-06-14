from kivy.app import App
from kivy.config import Config
import win32
import pywin
import os
import fonts
from kivy.graphics import Color, Rectangle
import runpy
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooser, FileChooserListView
from kivy.uix.label import Label
from kivy.graphics import Rectangle
import kivy.properties
from kivy.metrics import Metrics
from kivy.graphics.instructions import Instruction

LabelBase.register(name='JetbrainsMono',
                   fn_regular='fonts/JetBrainsMono[wght].ttf')

DEFAULT_FONT = 'JetbrainsMono'


class TabbedWindow(TabbedPanel):
    label_drag_n_drop = Label()
    color = ListProperty([1, 1, 1, 1])
    text_input = TextInput()
    text_output = TextInput(disabled=True)

    def __init__(self, **kwargs):
        super(TabbedWindow, self).__init__(**kwargs)
        self.do_default_tab = False
        self.tab_pos = 'top_mid'
        self.tab_width = 200
        # self.background_color = (1, 0, 0, .5)  # 50% translucent red
        # self.border = [0, 0, 0, 0]
        welcome_tab = TabbedPanelItem(text="Welcome!", font_family="JetbrainsMono")

        welcome_float_layout = FloatLayout()
        welcome_float_layout.add_widget(
            Label(text="Welcome to translator", font_family="JetbrainsMono", pos_hint={'y': .3}, font_size=25,
                  bold=True))
        welcome_float_layout.add_widget(
            Label(text="You can choose to translate the code either from Copy and Paste or File from the menu above.",
                  font_family="JetbrainsMono"))

        welcome_tab.add_widget(welcome_float_layout)

        self.add_widget(welcome_tab)
        self.home_tab = welcome_tab

        ################################
        input_tab = TabbedPanelItem(text="Read from input")
        bx = GridLayout(cols=2, padding=10)

        bx.add_widget(Label(text="Copy and paste the code in C++", font_family="JetbrainsMono", size_hint=(1, 0.1)))
        bx.add_widget(
            Label(text="Here is place for code translated to python ", font_family="JetbrainsMono", size_hint=(1, 0.1)))

        bx.add_widget(self.text_input)

        bx.add_widget(self.text_output)

        confirm_button = Button(text="Confirm", size_hint=(1, .1))
        bx.add_widget(confirm_button)
        confirm_button.bind(on_press=self.on_button_press_text)

        confirm_button = Button(text="Execute", size_hint=(1, .1))
        confirm_button.bind(on_press=self.on_button_press_execute)
        bx.add_widget(confirm_button)

        input_tab.add_widget(bx)

        self.add_widget(input_tab)

        ################################

        self.set_def_tab(welcome_tab)

        file_tab = TabbedPanelItem(text="Read from file", font_family="JetbrainsMono", bold=True)
        box_layout_file_tab = FloatLayout()
        box_layout_file_tab.add_widget(Label(text="Import a file", font_size=25, size_hint=(1, .1), pos_hint={'y': .9}))

        horizontal = BoxLayout(orientation='horizontal', pos_hint={'y': .8})
        horizontal.add_widget(
            Label(text="Paste the absolute path to file", font_family="JetbrainsMono", size_hint=(.3, .1)))
        path = TextInput(size_hint=(.7, .1))
        horizontal.add_widget(path)

        box_layout_file_tab.add_widget(horizontal)

        horizontal_1 = BoxLayout(orientation='horizontal', pos_hint={'y': .5})
        horizontal_1.add_widget(Label(text="Look for the file", size_hint=(.3, .3)))
        horizontal_1.add_widget(FileChooserListView(size_hint=(.7, .3)))
        box_layout_file_tab.add_widget(horizontal_1)

        self.label_drag_n_drop = Label(text="Or simply drag the file here!", size_hint=(1, 1), pos_hint={'y': -.2})

        box_layout_file_tab.add_widget(self.label_drag_n_drop)

        Window.bind(on_dropfile=self._on_file_drop)

        confirm_button_file = Button(text="Confirm and execute", size_hint=(1, .1), pos_hint={'y': 0})
        confirm_button_file.bind(on_press=self.on_button_press_file)
        box_layout_file_tab.add_widget(confirm_button_file)
        file_tab.add_widget(box_layout_file_tab)
        self.add_widget(file_tab)
        self.color = [175 / 255, 238 / 255, 238 / 255, 1]
        self.set_def_tab(welcome_tab)

    def _on_file_drop(self, window, file_path):
        self.label_drag_n_drop.color = [0, 1, 0, .8]

        with self.label_drag_n_drop.canvas:
            Color(0, 1, 1, 0.25)

        print(file_path)  ####filepath

        subprocess.call('start /wait python test.py', shell=True)

        return

    def on_button_press_text(self, arg):
        self.text_output.text = '''if __name__ == '__main__':
       str0 = input("Enter Your Name ")
       print("Hello ", str0, "!")
       '''
        return

    def on_button_press_file(self, arg):
        return

    def on_button_press_execute(self, arg):
        # exec(open('test.py').read())
        import subprocess
        subprocess.call('start /wait python test.py', shell=True)
        return


class MainWindow(App):

    def build(self):
        return TabbedWindow()


if __name__ == "__main__":
    MainWindow().run()
