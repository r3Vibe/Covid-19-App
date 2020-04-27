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
from kivymd.uix.label import MDLabel



#===================================classes for the screens===================================#
class ManageScreen(ScreenManager):
    pass

class ClosedCaseScreen(Screen):
    def go_to_close(self):
        self.manager.current = 'ClosedCaseScreen'
    def go_to_main(self):
        self.manager.current = 'MainScreen'

class LoadingScreen(Screen):
            
    def loadscreen(self):
        self.box1 = BoxLayout(orientation='horizontal', spacing=15)
        self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
        self.box.add_widget(MDLabel(halign= "center",text="It Will Take Some Time....",font_style="H4",theme_text_color= "Primary"))
        self.box.add_widget(self.box1)
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Ok",on_release= self.get_info))
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",on_release= self.PopDismiss))
        self.popup = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.box,
            size_hint=(1, .5),
        )
        self.popup.open()
        
    def get_info(self,*args):
        self.number = []
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.url = 'https://www.worldometers.info/coronavirus/country/india/'
        try:
            self.website = requests.get(self.url,headers=self.headers).text
        except:
            self.errormsg()
        else:
            self.soup = BeautifulSoup(self.website,'lxml')
            self.cc = self.soup.find("div", {"class": "number-table-main"}).string
            self.allinfo_numbers = self.soup.findAll(id="maincounter-wrap")
            for self.numbers in self.allinfo_numbers:
                self.number.append(self.numbers.span.text)       
            self.ClosedCases    =   self.cc.replace(",","").rstrip()
            self.TotalCases     =   self.number[0].replace(",","").rstrip()
            self.TotalDeaths    =   self.number[1].replace(",","").rstrip()
            self.TotalRecovery  =   self.number[2].replace(",","").rstrip()
            self.ActiveCases = (int(self.TotalCases) - int(self.ClosedCases))
            self.DeathR = round((int(self.TotalDeaths) / int(self.ClosedCases)) * 100)
            self.RecoverR = round((int(self.TotalRecovery) / int(self.ClosedCases)) * 100)
            self.changelabel()
            
    def retry(self,*args):
        self.popup2.dismiss()
        self.get_info()
            
    def changelabel(self,*args):
        self.popup.dismiss()
        self.manager.current = 'MainScreen'
        change = self.manager.get_screen("MainScreen")
        change.ti.text = str(self.TotalCases)
        change.td.text = str(self.ActiveCases)
        change.tr.text = str(self.ClosedCases)
        changeagain = self.manager.get_screen("ClosedCaseScreen")
        changeagain.tcn.text = str(self.ClosedCases)
        changeagain.tdn.text = str(self.TotalDeaths)
        changeagain.trn.text = str(self.TotalRecovery)
        changeagain.drn.text = str(self.DeathR)+"%"
        changeagain.rrn.text = str(self.RecoverR)+"%"

    def errormsg(self):
        self.popup.dismiss()
        self.box1 = BoxLayout(orientation='horizontal', spacing=15,padding=20)
        self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
        self.box.add_widget(MDLabel(halign= "center",text="Connection Error....",font_style="H4",theme_text_color= "Primary"))
        self.box.add_widget(self.box1)
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Retry",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.retry))
        self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.PopDismiss))
        self.popup2 = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.box,
            size_hint=(1, .5),
        )
        self.popup2.open()
        
    def PopDismiss(self,*args):
        exit()
            
class MainScreen(Screen):
    # def go_to_close(self):
    #     self.manager.current = 'ClosedCaseScreen'
    # def go_to_main(self):
    #     self.manager.current = 'MainScreen'
        
    # def refresh(self):
    #     self.box1 = BoxLayout(orientation='horizontal', spacing=15)
    #     self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
    #     self.box.add_widget(MDLabel(halign= "center",text="It Will Take Some Time....",font_style="H4",theme_text_color= "Primary"))
    #     self.box.add_widget(self.box1)
    #     self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Ok",on_release=self.get_info))
    #     self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",on_release=self.PopDismiss))
    #     self.popup = Popup(
    #         auto_dismiss=False,
    #         separator_height=0,
    #         title="",
    #         content=self.box,
    #         size_hint=(1, .5),
    #     )
    #     self.popup.open()

    # def PopDismiss(self,*args):
    #     exit()
        
    # def get_info(self,*args):
    #     self.headers = {'user-agent': 'Mozilla/5.0'}
    #     self.url = 'https://www.worldometers.info/coronavirus/country/india/'
    #     try:
    #         self.website = requests.get(self.url,headers=self.headers).text
    #     except:
    #         self.errormsg()
    #     else:
    #         self.number = []
    #         self.allinfo = BeautifulSoup(self.website,'lxml')
    #         self.allinfo_numbers = self.allinfo.findAll(id="maincounter-wrap")
    #         for self.numbers in self.allinfo_numbers:
    #                self.number.append(self.numbers.span.string)
    #         self.changelabel()

    # def changelabel(self):
    #     self.popup.dismiss()
    #     self.ti.text = str(self.number[0])
    #     self.td.text = str(self.number[1])
    #     self.tr.text = str(self.number[2])

    # def errormsg(self):
    #     self.popup.dismiss()
    #     self.box1 = BoxLayout(orientation='horizontal', spacing=15,padding=20)
    #     self.box = BoxLayout(orientation='vertical', spacing=15,padding=20)
    #     self.box.add_widget(MDLabel(halign= "center",text="Connection Error....",font_style="H4",theme_text_color= "Primary"))
    #     self.box.add_widget(self.box1)
    #     self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Retry",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.retry))
    #     self.box1.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.PopDismiss))
    #     self.popup2 = Popup(
    #         auto_dismiss=False,
    #         separator_height=0,
    #         title="",
    #         content=self.box,
    #         size_hint=(1, .5),
    #     )
    #     self.popup2.open()
    pass
#===================================classe for the navigation drawer===================================#
class ContentNavigationDrawer(BoxLayout):
    pass

        
#===================================classe for the kivy mainapp===================================#        
class MainApp(MDApp):
    def build(self):
        self.title = "Covid-19 Cases In India"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return ManageScreen()
        

#==This Will run the MainApp==# 
if __name__ == "__main__":
    MainApp().run()

