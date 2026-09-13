from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
import webbrowser

LINK = "https://script.google.com/a/macros/leroymerlin.com.br/s/AKfycbwBo_ETwXij_GqFNyagvIGgDJ2K8GdOPvbi27MoEBE/dev"

class Abastecimento3AApp(App):
    title = "Abastecimento 3A"

    def build(self):
        layout = BoxLayout(orientation="vertical", padding=dp(30), spacing=dp(20))
        layout.add_widget(Label(text="ABASTECIMENTO 3A", font_size="32sp", bold=True, size_hint_y=None, height=dp(80)))
        layout.add_widget(Label(text="Uma solução das Indústrias Kartazen", font_size="18sp", size_hint_y=None, height=dp(50)))
        layout.add_widget(Label(text="KARTAZEN\nSistema Inteligente de Abastecimento", font_size="20sp", bold=True, size_hint_y=None, height=dp(100)))
        layout.add_widget(Widget())
        botao = Button(text="ABRIR ABASTECIMENTO 3A", font_size="22sp", size_hint_y=None, height=dp(70))
        botao.bind(on_press=lambda *_: webbrowser.open(LINK))
        layout.add_widget(botao)
        return layout

Abastecimento3AApp().run()
