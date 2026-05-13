from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.1, 1)


class ComandoVozApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        titulo = Label(
            text="TR MARTINS IA",
            font_size=32,
            bold=True,
            color=(0, 1, 1, 1)
        )

        status = Label(
            text="Sistema iniciado",
            font_size=22,
            color=(1, 1, 1, 1)
        )

        botao = Button(
            text="ATIVAR COMANDO DE VOZ",
            size_hint=(1, 0.3),
            background_color=(0, 0.7, 1, 1),
            font_size=22
        )

        layout.add_widget(titulo)
        layout.add_widget(status)
        layout.add_widget(botao)

        return layout


ComandoVozApp().run()
