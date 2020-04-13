#Description: This Script will Scrape website to find the corona virus infected numbers
#and show the values in a kivy made gui

#===================================imports===================================#
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.font_definitions import theme_font_styles
import requests
from bs4 import BeautifulSoup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
#===================================imports===================================#


#===================================classes for the screens===================================#
class ManageScreen(ScreenManager):
    pass

class LoadingScreen(Screen):
    def calltwo(self):
        Clock.schedule_once(self.loadscreen,-1)
        Clock.schedule_once(self.update, 0)
    def update(self,*args):
        try:
            self.number = get_info()
            self.changelabel()
        except:
            MainApp.conn_work_dismiss(MainApp)
            MainApp.conn_error_popup(MainApp) 
        
    def changelabel(self):
        Clock.schedule_once(self.dismispop)
        self.manager.current = 'MainScreen'
        change = self.manager.get_screen("MainScreen")
        change.ti.text = str(self.number[0])
        change.td.text = str(self.number[1])
        change.tr.text = str(self.number[2])
        # return print("working well")
    
    def loadscreen(self,*args):
        MainApp.conn_working_popup(MainApp)
        # print("got to function")
    
    def dismispop(self,*args):
        MainApp.conn_work_dismiss(MainApp)



class MainScreen(Screen):
    def refresh(self):
        number = get_info()
        self.ti.text = str(number[0])
        self.td.text = str(number[1])
        self.tr.text = str(number[2])       
        # print("Works")

#===================================classes for the screens===================================#

#===================================classe for the navigation drawer===================================#
class ContentNavigationDrawer(BoxLayout):
    pass
#===================================classe for the navigation drawer===================================#
        
#===================================classe for the kivy mainapp===================================#        
class MainApp(MDApp):
    def build(self):
        self.title = "Covid-19 Cases In India"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return ManageScreen()

    def conn_working_popup(self):   
        self.dialog = MDDialog(
            text="Fetching Info...",
            size_hint=[.5,.5],
            )
        self.dialog.open()
    
    def conn_work_dismiss(self):
        MainApp.dialog.dismiss()

    def conn_error_popup(self):   
        self.dialog1 = MDDialog(
            text="Connection Error...",
            size_hint=[.5,.5],
            buttons=[
                MDFlatButton(
                    text="Close",
                    text_color= (1,1,1,1),
                    on_release=self.conn_error_dismiss
                ),
                MDFlatButton(
                    text="Retry",
                    text_color= (1,1,1,1),
                    on_release=self.retry
                ),
            ],
        )

        self.dialog1.open()
    def retry(self):
        pass

    def conn_error_dismiss(self):
        MainApp.dialog1.dismiss()
        exit()
#===================================classe for the kivy mainapp===================================#   

#==This function scrapes data from internet and returns the valus==#   
def get_info():
    headers = {'user-agent': 'Mozilla/5.0'}
    url = 'https://www.worldometers.info/coronavirus/country/india/'
    website = requests.get(url,headers=headers).text
    allinfo = BeautifulSoup(website,'lxml')
    allinfo_numbers = allinfo.findAll(id="maincounter-wrap")
    number = []
    for numbers in allinfo_numbers:
           number.append(numbers.span.string)
    return number
#==This function scrapes data from internet and returns the valus==# 

#==This Will run the MainApp==# 
if __name__ == "__main__":
    MainApp().run()
#==This Will run the MainApp==# 