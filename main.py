from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class MyFirstApp(App):
    def build(self):
        self.layout = FloatLayout()
        
        # Start with a white screen
        with self.layout.canvas.before:
            Color(1, 1, 1, 1) 
            self.rect = Rectangle(size=(2000, 2000), pos=(0,0))
            
        # Wait 5 seconds, then run the success function
        Clock.schedule_once(self.show_success, 5)
        return self.layout

    def show_success(self, dt):
        # Change background to Black
        with self.layout.canvas.before:
            Color(0, 0, 0, 1) 
            Rectangle(size=(2000, 2000), pos=(0,0))
            
        # Add the Neon Green Text
        success_label = Label(
            text="SUCCESS! U MADE UR\nTEST API/FIRST APP",
            color=(0, 1, 0, 1), 
            font_size='24sp',
            halign='center'
        )
        self.layout.add_widget(success_label)

if __name__ == '__main__':
    MyFirstApp().run()
