from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LinaGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.name_input = TextInput(
            hint_text="اكتب اسمك هنا",
            multiline=False,
            font_size=24,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.name_input)

        self.submit_button = Button(
            text="ابدأ اللعبة 🐾",
            font_size=24,
            size_hint=(1, 0.3),
            background_color=(0.3, 0.6, 0.8, 1)
        )
        self.submit_button.bind(on_press=self.start_game)
        self.add_widget(self.submit_button)

        self.output_label = Label(
            text="مرحبًا بك! أنا لينا، قطتك الافتراضية 🐱",
            font_size=22,
            halign="center",
            valign="middle"
        )
        self.add_widget(self.output_label)

    def start_game(self, instance):
        user_name = self.name_input.text.strip()
        if user_name:
            self.output_label.text = f"أهلًا {user_name}! أنا لينا وسأكون صديقتك الجديدة 😺"
        else:
            self.output_label.text = "من فضلك اكتب اسمك أولًا!"

class LinaApp(App):
    def build(self):
        self.title = "لينا - القطة الافتراضية"
        return LinaGame()

if __name__ == "__main__":
    LinaApp().run()
