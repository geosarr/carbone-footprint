
# from kivymd.app import MDApp
# from kivy.lang import Builder

# kv = """
# Screen:
#     MDLabel:
#         text: ""
#         id: txt
#         pos_hint: {'center_x': 0.5, 'center_y': 0.6}
#     MDRaisedButton:
#         text: 'Action Button'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#         on_press:
#             app.action()
#     MDRoundFlatButton:
#         text: 'MDRoundFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#     MDRectangleFlatButton:
#         text: 'MDRectangleFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#     MDRectangleFlatIconButton:
#         text: 'MDRectangleFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.2}
#         width: dp(230)
#         icon: 'google'
#     MDFillRoundFlatIconButton:
#         text: 'MDFillRoundFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.1}
#         width: dp(230)
#         icon: 'google'
#     MDFloatingActionButtonSpeedDial:
#         data: app.more
#         rotation_root_button: True
# """


# class Main(MDApp):
#     more = {
#         "Python": "language-python",
#         "Rust": "language-rust",
#         "C++": 'language-cpp'
#     }

#     def action(self):
#         label = self.root.ids.txt
#         label.text = "This text is displayed after pressing button"

#     def build(self):
#         return Builder.load_string(kv)


# Main().run()




# from kivymd.app import MDApp
# from kivy.lang import Builder
# from plyer import accelerometer

# kv = """
# Screen:
#     MDLabel:
#         text: ""
#         id: txt
#         pos_hint: {'center_x': 0.5, 'center_y': 0.6}
#     MDRaisedButton:
#         text: 'Action Button'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#         on_press:
#             app.action()
#     MDRoundFlatButton:
#         text: 'MDRoundFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#     MDRectangleFlatButton:
#         text: 'MDRectangleFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#     MDRectangleFlatIconButton:
#         text: 'MDRectangleFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.2}
#         width: dp(230)
#         icon: 'google'
#     MDFillRoundFlatIconButton:
#         text: 'MDFillRoundFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.1}
#         width: dp(230)
#         icon: 'google'
#     MDFloatingActionButtonSpeedDial:
#         data: app.more
#         rotation_root_button: True
# """


# class Main(MDApp):
#     more = {
#         "Python": "language-python",
#         "Rust": "language-rust",
#         "C++": 'language-cpp'
#     }

#     def action(self):
#         label = self.root.ids.txt
#         label.text = "This text is displayed after pressing button"

#     def build(self):
#         return Builder.load_string(kv)


# Main().run()


# from kivymd.app import MDApp
# from kivy.lang import Builder
# from plyer import accelerometer

# kv = """
# Screen:
#     MDLabel:
#         text: ""
#         id: txt
#         pos_hint: {'center_x': 0.5, 'center_y': 0.6}
#     MDRaisedButton:
#         text: 'Action Button'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#         on_press:
#             app.action()
#     MDRoundFlatButton:
#         text: 'MDRoundFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#     MDRectangleFlatButton:
#         text: 'MDRectangleFlatButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#     MDRectangleFlatIconButton:
#         text: 'MDRectangleFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.2}
#         width: dp(230)
#         icon: 'google'
#     MDFillRoundFlatIconButton:
#         text: 'MDFillRoundFlatIconButton'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.1}
#         width: dp(230)
#         icon: 'google'
#     MDFloatingActionButtonSpeedDial:
#         data: app.more
#         rotation_root_button: True
# """


# class Main(MDApp):
#     more = {
#         "Python": "language-python",
#         "Rust": "language-rust",
#         "C++": 'language-cpp'
#     }

#     def action(self):
#         label = self.root.ids.txt
#         label.text = "This text is displayed after pressing button"

#     def build(self):
#         return Builder.load_string(kv)


# Main().run()

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.clock import Clock
from plyer import accelerometer, gravity


class Sensors(Widget):
    def __init__(self):
        super(Sensors, self).__init__()
        self.sensorEnabled = False

    def get_acceleration(self, dt):
        accel = accelerometer.acceleration

        self.ids.label1_acc.text = f"acc_x: {accel[0]}"
        self.ids.label2_acc.text = f"acc_y: {accel[1]}"
        self.ids.label3_acc.text = f"acc_z: {accel[2]}"

        acc_mag = ((accel[0])**2 + (accel[1])**2 + (accel[2])**2)**(1/2)
        self.ids.label4_acc.text = f"acc mag: {acc_mag}"

    # def get_gravity(self):
    #     grav = gravity.gravity

    #     self.ids.label1_grav.text = f"grav_x: {grav[0]}"
    #     self.ids.label2_grav.text = f"grav_y: {grav[1]}"
    #     self.ids.label3_grav.text = f"grav_z: {grav[2]}"


    #     grav_mag = ((grav[0])**2 + (grav[1])**2 + (grav[2])**2)**(1/2)
    #     self.ids.label4_grav.text = f"grav mag: {grav_mag}"

    def pressed1(self):
        try:
            if not self.sensorEnabled:
                accelerometer.enable()
                # gravity.enable()
                Clock.schedule_interval(self.get_acceleration, 1 / 20.)
                # Clock.schedule_interval(self.get_gravity, 1 / 20.)

                self.sensorEnabled = True
                self.ids.button1.text = "Stop"
            else:
                accelerometer.disable()
                # gravity.disable()
                Clock.unschedule(self.get_acceleration)
                # Clock.unschedule(self.get_gravity)

                self.sensorEnabled = False
                self.ids.button1.text = "Start"
        except NotImplementedError:
            import traceback; traceback.print_exc()
            self.ids.status.text = "accelerometer or gravity is not supported for your platform"

class SensorsApp(App):
    def build(self):
        return Sensors()

SensorsApp().run()