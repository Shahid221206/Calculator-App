import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from math import sin, cos, tan, log, sqrt, factorial, exp

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/", "%", "**", "sin", "cos", "tan", "log", "ln", "sqrt", "!", "x^2", "x^3"]
        self.memory = 0
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.result_input = TextInput(
            font_size=32, 
            readonly=True, 
            halign="right", 
            multiline=False, 
            background_color=[1, 1, 1, 1], 
            foreground_color=[0, 0, 0, 1]
        )
        main_layout.add_widget(self.result_input)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "DEL", "+"],
            ["C", "(", ")", "="],
            ["sin", "cos", "tan", "log"],
            ["ln", "sqrt", "x^2", "x^3"],
            ["!", "M+", "MR", "MC"],
            ["exp", "e", "π"]
        ]

        for row in buttons:
            h_layout = GridLayout(cols=4, spacing=10)
            for label in row:
                button = Button(
                    text=label, 
                    font_size=24, 
                    on_press=self.on_button_press,
                    background_color=[0.8, 0.8, 0.8, 1],
                    color=[0, 0, 0, 1]
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.result_input.text
        button_text = instance.text

        if button_text == "C":
            self.result_input.text = ""
        elif button_text == "DEL":
            self.result_input.text = current[:-1]
        elif button_text == "=":
            try:
                expression = self.result_input.text.replace("x^2", "**2").replace("x^3", "**3").replace("sqrt", "sqrt")
                expression = expression.replace("sin", "sin").replace("cos", "cos").replace("tan", "tan")
                expression = expression.replace("log", "log10").replace("ln", "log").replace("!", "factorial")
                expression = expression.replace("exp", "exp").replace("e", str(exp(1))).replace("π", str(3.141592653589793))
                self.result_input.text = str(eval(expression))
            except Exception:
                self.result_input.text = "Error"
        elif button_text == "M+":
            try:
                self.memory = eval(self.result_input.text)
            except Exception:
                self.result_input.text = "Error"
        elif button_text == "MR":
            self.result_input.text = str(self.memory)
        elif button_text == "MC":
            self.memory = 0
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.result_input.text += button_text

        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

if __name__ == "__main__":
    CalculatorApp().run()
