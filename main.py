# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.uix.popup import Popup

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
        if not surveyComplete:
            sm.current = "surveyInfo"
        else:
            popup = Popup(title='Survey Already Taken',
            content=Label(text='You have already taken the daily survey'),
            size_hint=(None, None), size=(400, 400))
            popup.open()

    def getData(self):
        sm.current = "data"

    def getCode(self):
        if surveyComplete:
            sm.current = "healthy"
        else:
            popup = Popup(title='View Results',
            content=Label(text='Please complete the survey to view your results'),
            size_hint=(None, None), size=(400, 400))
            popup.open()

    def logout(self):
        sm.current = "login"

class DailySurveyInfo(Screen):
    def back(self):
        sm.current = "main"
    def startSurvey(self):
        sm.current = "survey"
    
class DailySurvey(Screen):
    def contSurvey(self):
        sm.current = "survey2"
        
class DailySurveyTwo(Screen):
    def contSurvey(self):
        sm.current = "survey3"
    def back(self):
        sm.current = "survey"

class DailySurveyThree(Screen):
    def submitSurvey(self):
        global surveyComplete
        sm.current = "healthy"
        surveyComplete = True
    def back(self):
        sm.current = "survey2"

class CheckBoxLayout(Screen):
    pass

class HealthyWindow(Screen):
    pass

class WarningWindow(Screen):
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

surveyComplete = False
kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), DailySurveyInfo(name="surveyInfo"), DailySurvey(name="survey"), DailySurveyTwo(name="survey2"), DailySurveyThree(name="survey3"), HealthyWindow(name="healthy"), WarningWindow(name="warning"), SchoolData(name="data")]

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