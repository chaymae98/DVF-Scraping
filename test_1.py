
import select
from time import sleep

import pandas
import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



class CadastreAPI(object):
    url = "https://www.cadastre.gouv.fr/scpc/accueil.do"

    # dataframe result
    list_parc = []

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.xl = "Exemples Biens - SCI SA.csv"
        # self.xl = "test.csv"

    def close(self):
        self.driver.close()
    import pandas as pd

    # exemple de biens


    # réécriture : factorisation du code
    def liste_biens(self, csv_file=None):
        if csv_file is None:
            csv_file = self.xl
        biens = pd.read_csv(filepath_or_buffer=csv_file, sep=";", encoding_errors='ignore')
        return biens[biens.columns[:4]]

 #   info = liste_biens()
#    print(info.head())

    def scraping(self, numero_voie, nom_voie, nom_ville, code_postal):
        driver = self.driver
        driver.get(__class__.url)



        els = {'numero': ('id', 'numeroVoie', numero_voie,),
               'voie': ('name', "nomVoie", nom_voie,),
               'ville': ('id', "ville", nom_ville),
               'code_postal': ('id', "codePostal", code_postal,)}
        last_el = None
        for el, el_info in els.items():
            if el_info[0] == 'name':
                form = driver.find_element_by_name(el_info[1])
                print("t")
            elif el_info[0] == 'id':
                form = driver.find_element_by_id(el_info[1])

            x = el_info[2]
            print(x, type(x))
            if type(x) == float:
                x = int(x)
            elif type(x) == str:
                x = str(x)
            else:
                x = str(x)
            print(x, type(x))

            form.click()
            form.clear()
            form.send_keys(str(el_info[2]))



            last_el = form
        form.send_keys(Keys.ENTER)

        req = requests.get("https://www.cadastre.gouv.fr/scpc/accueil.do")
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            # pdb.set_trace():
            # breakpoint()

            parselle = driver.find_element_by_class_name("parcelles").find_element_by_class_name("nomcol")

            print(parselle.text)
            if str(parselle.text).lower().find("parcelle") >= 0:
                out = parselle.text
                parc = out.replace("Parcelle n° ", "").replace(" Feuille 000 ", "").replace(" 01 ", "").replace(" Commune : ", "")
                parc_array = parc.split("-")
                self.list_parc.append(parc_array)

            """j = len(parselle.text)
            i = 0
            with open("donnees1.csv", "w", encoding="utf-8") as fichier:
                writer = csv.writer(fichier)
                while i < j:
                    writer.writerow((parselle.text[i]))
                    i += 1
            
            with open('données.csv','w',newline="")as f_output:
                csv_output= csv.writer(f_output)
                csv_output.writerows(rows)

            donnees_a_exporter_dataframe= pandas.DataFrame(rows)
            print(donnees_a_exporter_dataframe)"""

        except:
            out = None
            print("pas de parcelle")



        return self.list_parc


if __name__ == '__main__':
    api = CadastreAPI()
    liste_bien = api.liste_biens()
    #print(liste_bien.loc[0])
    #print(liste_bien.loc[0])
    #print(liste_bien.loc[0])

    list_parcs = []

    #i=0

    for index, row in liste_bien.iterrows():
            '''if i == 4:
                break'''
            print("test", index, row)
            list_parcs = api.scraping((row["N BIEN"]), row["ADRESSE"], row["VILLE"], row["CODE POSTAL"])

            # pour les tests
            #i = i + 1
            #api.scraping(row[0], row[1], row[3], row[2])
            #api.scraping(liste_bien.loc[0])
            #pi.scraping([0],[1],[3],[2])
            # if [59] == 'NaN':
            #    print('en effet je marche')
            #    break

    api.close()
    # breakpoint()

    df = pd.DataFrame(list_parcs)

    df.columns = ['NO_PARC', 'FEUILLE', 'COMMUNE']
    #del df['COMMUNE']
    #new_df = pd.DataFrame.assign('DEPARTEMENT')

    df.to_csv("donnees_parcelles2.csv", index=False)



    #def extraire_donees(url):

    """req = requests.get("https://www.cadastre.gouv.fr/scpc/rechercherPlan.do")
        soup = BeautifulSoup(req.text, "html.parser")
        print("The href are :")
        for text in soup.find_all("a"):
            print(text.get('href'))
        for text in soup.find("tbody", class_="parcelles").find("td", class_="nomcol"):
            print(text.get('a'))
        onglet_div=soup.find("tbody", class_="parcelles")
        parcelles=onglet_div.find("td", class_="nomcol")
        for text in soup.find_all('a'):
            print(text.get('href'))
    
    
    api.scraping(numero_voie= [0], nom_voie= [1], nom_ville= [2], code_postal= [3])
    
    
    with open("donnees.csv", "w", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
    
    
    j = len(parselle.text)
    i = 0
    with open("donnees.csv", "w", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        while i < j:
            writer.writerow((parselle.text[i]))
            i += 1
    """
