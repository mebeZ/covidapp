# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    osis = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.osis.text != "":
            if self.password != "":
                db.add_user(self.osis.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.osis.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    osis = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.osis.text, self.password.text):
            MainWindow.current = self.osis.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.osis.text = ""
        self.password.text = ""


class MainWindow(Screen):
    def takeSurvey(self):
        sm.current = "survey"

    def getData(self):
        sm.current = "data"

    def getCode(self):
        sm.current = "code"

    def logout(self):
        sm.current = "login"

class DailySurvey(Screen):
    pass

class QRCode(Screen):
    pass

class SchoolData(Screen):
    pass


class WindowManager(ScreenManager):
    pass 

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), DailySurvey(name="survey"), QRCode(name="code"), SchoolData(name="data")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm

    def goToMain(self):
        sm.current = "main"


if __name__ == "__main__":
    MyMainApp().run()