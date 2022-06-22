import subprocess

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.graphics import Color
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from pygments.styles import get_style_by_name


from CppToPython import CppToPython

LabelBase.register(name='JetbrainsMono',
                   fn_regular='fonts/JetBrainsMono[wght].ttf')

DEFAULT_FONT = 'JetbrainsMono'


class TabbedWindow(TabbedPanel):
    label_drag_n_drop = Label()
    color = ListProperty([1, 1, 1, 1])
    style = get_style_by_name("zenburn")

    text_input = CodeInput(font_family="JetbrainsMono", style=style, background_color=style.background_color)
    text_output = CodeInput(font_family="JetbrainsMono", style=style, background_color=style.background_color)
    errors_text_input_text_tab = TextInput()
    errors_text_input_file_tab = TextInput()

    text_out_str = R""

    text_output.text = text_out_str

    path_to_file = TextInput()

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

        bx = GridLayout(cols=4, padding=10)

        bx.add_widget(Label(size_hint=(.001, 0.1)), index=0)
        bx.add_widget(Label(text="Copy and paste the code in C++", font_family="JetbrainsMono", size_hint=(1, 0.1)),
                      index=0)
        bx.add_widget(
            Label(text="Here is place for code translated to python ", font_family="JetbrainsMono", size_hint=(1, 0.1)),
            index=0)

        bx.add_widget(Label(size_hint=(.001, .1)), index=0)

        bx.add_widget(Label(text="1", size_hint=(.001, 1)))
        bx.add_widget(self.text_input, index=0)

        # self.text_output._enable_scroll = True

        bx.add_widget(self.text_output)

        # TODO
        bx.add_widget(Label(size_hint=(.001, .1)))

        bx.add_widget(Label(size_hint=(.001, .1)))

        confirm_button = Button(text="Translate", size_hint=(1, .1))
        bx.add_widget(confirm_button)

        confirm_button.bind(on_press=self.on_button_press_text)

        execute_button = Button(text="Execute", size_hint=(1, .1))
        execute_button.bind(on_press=self.on_button_press_execute)
        bx.add_widget(execute_button)
        bx.add_widget(Label(size_hint=(.001, .1)))

        box_layout = BoxLayout(orientation='vertical')
        bx.size_hint = (1, .9)
        box_layout.add_widget(bx)

        self.errors_text_input_text_tab.size_hint = (1, .05)
        self.errors_text_input_text_tab._enable_scroll = True

        box_layout.add_widget(self.errors_text_input_text_tab)

        input_tab.add_widget(box_layout)

        self.add_widget(input_tab)

        ################################

        self.set_def_tab(welcome_tab)

        file_tab = TabbedPanelItem(text="Read from file", font_family="JetbrainsMono")
        box_layout_file_tab = FloatLayout()
        box_layout_file_tab.add_widget(Label(text="Import a file", font_size=25, size_hint=(1, .1), pos_hint={'y': .9}))

        horizontal = BoxLayout(orientation='horizontal', pos_hint={'y': .5})
        horizontal.add_widget(
            Label(text="Paste the absolute path to file", font_family="JetbrainsMono", size_hint=(.3, .1)))

        self.path_to_file.size_hint = (.7, .1)
        horizontal.add_widget(self.path_to_file)

        box_layout_file_tab.add_widget(horizontal)

        confirm_button_file = Button(text="Confirm and execute", size_hint=(1, .1), pos_hint={'y': .05})
        confirm_button_file.bind(on_press=self.on_button_press_file)
        box_layout_file_tab.add_widget(confirm_button_file)

        self.errors_text_input_file_tab.pos_hint = {'y': 0, 'x': 0}
        self.errors_text_input_file_tab.size_hint = (1, .05)
        self.errors_text_input_file_tab._enable_scroll = True

        box_layout_file_tab.add_widget(self.errors_text_input_file_tab)

        input_tab.add_widget(box_layout)

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
        translator = CppToPython()
        self.text_output.text = translator.from_string(self.text_input.text)
        self.update_errors()
        return

    def update_errors(self):
        with open("dist_tmp/diag.txt", "r") as file:
            errors_str = file.readline()
            self.errors_text_input_text_tab.text = errors_str
            self.errors_text_input_file_tab = errors_str
        self.errors_text_input_text_tab.cursor = (0, 0)

    def on_button_press_file(self, arg):
        path = str(self.path_to_file.text)

        if not path.endswith(".cpp") and not path.endswith(".txt"):
            popup = Popup(title='Incorrect path to file',
                          content=Label(text="Enter correct path to file, ending with .txt or .cpp"),
                          size_hint=(.5, .2), auto_dismiss=True)
            self.path_to_file.text = ""
            popup.open()
            return

        path.replace("\\", "/")
        translator = CppToPython()
        out = path.removesuffix(".cpp")
        out.removesuffix(".txt")
        out += ".py"
        translator.from_file(path, out)

        self.update_errors()

        subprocess.call(f'start /wait python {out}', shell=True)
        return

    @staticmethod
    def on_button_press_execute(arg):
        # exec(open('test.py').read())
        subprocess.call('start /wait python out.py', shell=True)
        return


class MainWindow(App):

    def build(self):
        return TabbedWindow()


if __name__ == "__main__":
    MainWindow().run()
