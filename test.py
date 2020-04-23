import requests
from bs4 import BeautifulSoup

class testThis():
    def info(self):
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.url = 'https://www.worldometers.info/coronavirus/country/india/'
        self.website = requests.get(self.url,headers=self.headers).text
        self.number = []
        self.soup = BeautifulSoup(self.website,'lxml')
        self.cc = self.soup.find("div", {"class": "number-table-main"}).string
        self.allinfo_numbers = self.soup.findAll(id="maincounter-wrap")
        for self.numbers in self.allinfo_numbers:
            self.number.append(self.numbers.span.text)       

        self.ClosedCases    =   self.cc.replace(",","").rstrip()
        self.TotalCases     =   self.number[0].replace(",","").rstrip()
        self.TotalDeaths    =   self.number[1].replace(",","").rstrip()
        self.TotalRecovery  =   self.number[2].replace(",","").rstrip()
        
        
        
        
if __name__ == '__main__':
    testThis().run()
    


self.ActiveCases = int(TotalCases) - int(ClosedCases)
self.DeathR = round((int(TotalDeaths) / int(ClosedCases)) * 100)
self.RecoverR = round((int(TotalRecovery) / int(ClosedCases)) * 100)

print("Active: "+str(ActiveCases))
print("Closed: "+str(ClosedCases))
print("Death: "+str(TotalDeaths))
print("Recovery: "+str(TotalRecovery))
print("Death Ratio: "+str(DeathR) + "%")
print("Recovery Ratio: "+str(RecoverR) + "%")
