import select

import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selenium permet de lancer un navigateur web
driver = webdriver.Chrome()
print(type(driver))

# ouvrir la page web
url = "https://cuisine.journaldesfemmes.fr/recette/333415-recette-de-crepes-la-meilleure-recette-rapide"
print("lancement navigateur")
driver.get(url)


req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
print("The href links are:")
for text in soup.find_all('div'):
    print(text.get('li'))




"""soup = BeautifulSoup()
div_= soup.find(div, class_ ="parcelles")
tbody_parcelles_tr=div_.find_all("tr")
print()

#tbody_parcelles= driver.find_elements_by_class_name("nomcol")

tbody_parcelles = soup.find("tbody", class_="parcelles")
   tbody_parcelles_tr = tbody_parcelles.find_all("tr")"""

"""driver = webdriver.Chrome()
print(type(driver))

url = "https://www.cadastre.gouv.fr/scpc/rechercherPlan.do"
print("lancement navigateur")
driver.get(url)



soup = BeautifulSoup()
tbody_parcelles= soup.find("tbody", class_ ="parcelles")
tbody_parcelles_tr=tbody_parcelles.find_all("tr")
print()"""

for index, row in liste_bien.iterrows():
    print("test", index, row)
    api.scraping((row["N BIEN"]), row["ADRESSE"], row["VILLE"], row["CODE POSTAL"])

    if __name__ == "__main__":
        api = CadastreAPI()
        liste_bien = api.liste_biens()

