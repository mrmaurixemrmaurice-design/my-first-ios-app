from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class MyFirstApp(App):
    def build(self):
        self.layout = FloatLayout()
        # Step 1: Start with a white background
        with self.layout.canvas.before:
            Color(1, 1, 1, 1) 
            self.rect = Rectangle(size=(3000, 3000), pos=(-500,-500))
            
        # Step 2: Wait 5 seconds then trigger the success screen
        Clock.schedule_once(self.show_success, 5)
        return self.layout

    def show_success(self, dt):
        # Step 3: Change background to Green
        with self.layout.canvas.before:
            Color(0, 1, 0, 1) 
            Rectangle(size=(3000, 3000), pos=(-500,-500))
            
        # Step 4: Add Black text
        success_label = Label(
            text="SUCCESS!",
            color=(0, 0, 0, 1), 
            font_size='50sp',
            bold=True
        )
        self.layout.add_widget(success_label)

if __name__ == '__main__':
    MyFirstApp().run()
