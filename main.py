#Description: This Script will Scrape website to find the corona virus infected numbers
#and show the values in a kivy made gui

#===================================imports===================================#
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
from bs4 import BeautifulSoup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#===================================imports===================================#


#===================================classes for the screens===================================#
class ManageScreen(ScreenManager):
    pass

class LoadingScreen(Screen):
    def get_info(self,*args):
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.url = 'https://www.worldometers.info/coronavirus/country/india/'
        try:
            self.website = requests.get(self.url,headers=self.headers).text
        except:
            self.errormsg()
        else:
            self.number = []
            self.allinfo = BeautifulSoup(self.website,'lxml')
            self.allinfo_numbers = self.allinfo.findAll(id="maincounter-wrap")
            for self.numbers in self.allinfo_numbers:
                   self.number.append(self.numbers.span.string)
            self.changelabel()
        
    def loadscreen(self):
        self.box1 = BoxLayout(orientation='horizontal', spacing=15)
        self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
        self.box.add_widget(Label(text="This Will Take Some Time....",font_size=25,color=(1,.5,.2,1)))
        self.box.add_widget(self.box1)
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Ok",theme_text_color= "Custom",text_color= (1,1,1,1),on_release=self.get_info))
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (1,1,1,1),on_release=self.PopDismiss))
        self.popup = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.box,
            size_hint=(1, .5),
        )
        self.popup.open()
        
    def retry(self,*args):
        self.popup2.dismiss()
        self.get_info()
            
    def changelabel(self):
        self.popup.dismiss()
        self.manager.current = 'MainScreen'
        change = self.manager.get_screen("MainScreen")
        change.ti.text = str(self.number[0])
        change.td.text = str(self.number[1])
        change.tr.text = str(self.number[2])

    def errormsg(self):
        self.popup.dismiss()
        self.box1 = BoxLayout(orientation='horizontal', spacing=15)
        self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
        self.box.add_widget(Label(text="Connection Error...",font_size=25,color=(1,.5,.2,1)))
        self.box.add_widget(self.box1)
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Retry",theme_text_color= "Custom",text_color= (1,1,1,1),on_release=self.retry))
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (1,1,1,1),on_release=self.PopDismiss))
        self.popup2 = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.box,
            size_hint=(1, .5),
        )
        self.popup2.open()
        
    def PopDismiss(self):
        exit()
            
class MainScreen(Screen):
    def refresh(self):
        # number = get_info()
        # self.ti.text = str(number[0])
        # self.td.text = str(number[1])
        # self.tr.text = str(number[2])       
        # # print("Works")
        pass

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

#===================================classe for the kivy mainapp===================================#   

#==This function scrapes data from internet and returns the valus==#   

#==This function scrapes data from internet and returns the valus==# 

#==This Will run the MainApp==# 
if __name__ == "__main__":
    MainApp().run()
#==This Will run the MainApp==# 