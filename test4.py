import select
from time import sleep
import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


def nettoyer_texte(t):
    return t.replace("\xa0", "").replace("\n", "").strip()


class CadastreAPI(object):
    url = "https://www.cadastre.gouv.fr/scpc/accueil.do"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.xl = "Exemples Biens - SCI SA.csv"

    def liste_biens(self, csv_file=None):
        if csv_file is None:
            csv_file = self.xl
        biens = pd.read_csv(filepath_or_buffer=csv_file, sep=";", encoding_errors='ignore')
        return biens[biens.columns[:4]]

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

            x= el_info [2]
            print(x,type(x))
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

        div_recettes = soup.find("div", id="recettes")
        ul_recettes = div_recettes.find("ul",recursive=False)
        li_recettes = ul_recettes.find_all("li")

        liste_resultats = []
        for li in li_recettes:

        def retraitement_adresse(df_info):
            pdf = process_num(pd.DataFrame(data=df_info['ADRESSE']))
            for c in df_info.columns:
                if not (c in pdf.columns):
                    pdf[c] = df_info[c]
            return pdf




api = CadastreAPI()
liste_bien = api.liste_biens()
print(liste_bien)
for index, row in liste_bien.iterrows():
    print("test", index, row)
    api.scraping((row["N BIEN"]), row["ADRESSE"], row["VILLE"], row["CODE POSTAL"])
    if [59] == 'NaN':
        print('en effet je marche')
        break
api.close()

