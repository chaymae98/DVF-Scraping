import  select
from time import sleep
import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

import pdb


class CadastreAPI(object):
    url = "https://www.cadastre.gouv.fr/scpc/accueil.do"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def scraping(self, numero_voie, nom_voie, nom_ville, code_postal):

        driver = self.driver
        driver.get(__class__.url)

        els = {'numero': ('id', "numeroVoie", numero_voie),
               'voie': ('name', "nomVoie", nom_voie),
               'ville': ('id', "ville", nom_ville),
               'code_postal': ('id', "codePostal", code_postal)}

        for el in els.keys():
            el_info = els[el]
            if el_info[0] == 'name':
                form = driver.find_element_by_name(el_info[1])
            elif el_info[0] == 'id':
                form = driver.find_element_by_id(el_info[1])

            form.click()
            form.clear()
            form.send_keys(el_info[2])

        # pdb.set_trace()
        form.send_keys(Keys.ENTER)

        out = None
        req = requests.get("https://www.cadastre.gouv.fr/scpc/accueil.do")
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            # pdb.set_trace()
            tbody= soup.find_all('tbody', class_="parcelles")
            parselle = driver.find_element_by_class_name("parcelles").find_element_by_class_name("nomcol")
            # pdb.set_trace()
            print(parselle.text)
            if str(parselle.text).lower().find("parcelle") >= 0:
                out = (parselle.text)
        finally:
            driver.close()

        return out

    def scraping_all(self, df, cols):
        df['Output_Cadastre'] = None
        for i, immo in df[cols].iterrows():
            parcelle = self.scraping(numero_voie=immo[0], nom_voie=immo[1], nom_ville=immo[2],
                                     code_postal=str(int(immo[3])))

            if parcelle is not None:
                df['Output_Cadastre'].at[i] = parcelle

        return df


# demo
if __name__ == "__main__":
    api = CadastreAPI()
    api.scraping('45', 'rue poncelet', '', '75017')