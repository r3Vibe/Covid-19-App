from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.boxlayout import BoxLayout
import requests
from bs4 import BeautifulSoup

class SwapScreen(ScreenManager):
    pass


class ClosedCases(Screen):
       
    def change_Screen_all(self,*args):
        self.manager.current = "MainScreen"
    
    def change_Screen_Closed(self,*args):
        self.manager.current = "ClosedCases"  
       
    def askif(self,*args):
        self.boxwithbutton = BoxLayout(orientation="horizontal",padding=15,spacing=15)
        self.boxwithmsg = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxcontain = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxwithmsg.add_widget(MDLabel(halign="center",font_style="H4",theme_text_color="Primary",text="Are You Sure?"))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Yes",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.close))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="No",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.dis))
        self.boxcontain.add_widget(self.boxwithmsg)
        self.boxcontain.add_widget(self.boxwithbutton)
        self.askmsg = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.boxcontain,
            size_hint=(1, .5),   
        )
        self.askmsg.open()  
    
    def dis(self,*args):
        self.askmsg.dismiss()
    
    def close(self,*args):
        exit()
        
class GetInfoScreen(Screen):
    
    promtmsg = False
    againmsg = False
    
    def prompt(self):
        self.promtmsg = True
        self.againmsg = False
        self.boxwithbutton = BoxLayout(orientation="horizontal",padding=15,spacing=15)
        self.boxwithmsg = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxcontain = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxwithmsg.add_widget(MDLabel(halign="center",font_style="H4",theme_text_color="Primary",text="It Will Take Some Time!!"))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Okay",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.getinfo))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.close))
        self.boxcontain.add_widget(self.boxwithmsg)
        self.boxcontain.add_widget(self.boxwithbutton)
        self.confirm = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.boxcontain,
            size_hint=(1, .5),   
        )
        self.confirm.open()
        
    def close(self,*args):
        exit()
    
    def getinfo(self,*args):
        if self.promtmsg == True:
            self.confirm.dismiss()
        elif self.againmsg == True:
            self.again.dismiss()
        self.number = []
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.url = 'https://www.worldometers.info/coronavirus/country/india/'
        try:
            self.website = requests.get(self.url,headers=self.headers,timeout=5).text
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
            self.update()
        
    def errormsg(self,*args):
        self.confirm.dismiss()
        self.boxwithbutton = BoxLayout(orientation="horizontal",padding=15,spacing=15)
        self.boxwithmsg = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxcontain = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxwithmsg.add_widget(MDLabel(halign="center",font_style="H4",theme_text_color="Primary",text="Unable To Contact The Server!"))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Try Again",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.retry))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.close))
        self.boxcontain.add_widget(self.boxwithmsg)
        self.boxcontain.add_widget(self.boxwithbutton)
        self.error = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.boxcontain,
            size_hint=(1, .5),   
        )
        self.error.open()        
    
    def retry(self,*args):
        self.promtmsg = False
        self.againmsg = True
        self.error.dismiss()
        self.boxwithbutton = BoxLayout(orientation="horizontal",padding=15,spacing=15)
        self.boxwithmsg = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxcontain = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxwithmsg.add_widget(MDLabel(halign="center",font_style="H4",theme_text_color="Primary",text="This Will Take Some Time!"))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Okay",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.getinfo))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Exit",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.close))
        self.boxcontain.add_widget(self.boxwithmsg)
        self.boxcontain.add_widget(self.boxwithbutton)
        self.again = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.boxcontain,
            size_hint=(1, .5),   
        )
        self.again.open()     
    
    def update(self,*args):
        self.promtmsg = False
        self.againmsg = False   
        self.manager.current = "MainScreen" 
        change = self.manager.get_screen("MainScreen")
        change.ti.text = str(self.TotalCases)
        change.ac.text = str(self.ActiveCases)
        change.cc.text = str(self.ClosedCases)
        closed = self.manager.get_screen("ClosedCases")
        closed.trn.text = str(self.TotalRecovery)
        closed.tdn.text = str(self.TotalDeaths)
        closed.tcc.text = str(self.ClosedCases)
        closed.dr.text = str(self.DeathR) + " %"
        closed.rr.text = str(self.RecoverR) + " %"

class MainScreen(Screen):
    def askif(self,*args):
        self.boxwithbutton = BoxLayout(orientation="horizontal",padding=15,spacing=15)
        self.boxwithmsg = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxcontain = BoxLayout(orientation="vertical",padding=15,spacing=15)
        self.boxwithmsg.add_widget(MDLabel(halign="center",font_style="H4",theme_text_color="Primary",text="Are You Sure?"))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="Yes",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.close))
        self.boxwithbutton.add_widget(MDFillRoundFlatButton(font_size=20,text="No",theme_text_color= "Custom",text_color= (0,0,0,0),on_release=self.dis))
        self.boxcontain.add_widget(self.boxwithmsg)
        self.boxcontain.add_widget(self.boxwithbutton)
        self.askmsg = Popup(
            auto_dismiss=False,
            separator_height=0,
            title="",
            content=self.boxcontain,
            size_hint=(1, .5),   
        )
        self.askmsg.open()  
    
    def dis(self,*args):
        self.askmsg.dismiss()
        
    def close(self,*args):
        exit()
        
    def change_Screen_all(self,*args):
        self.manager.current = "MainScreen"
    
    def change_Screen_Closed(self,*args):
        self.manager.current = "ClosedCases"     
    

class ContentNavigationDrawer(BoxLayout):
    pass
          
class MainApp(MDApp):
    def build(self):
        self.title = "Covid-19 Updates"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return SwapScreen()  
    
MainApp().run()
