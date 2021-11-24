#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

class CadastreAPI(object):
    url = "https://www.cadastre.gouv.fr/scpc/accueil.do"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.xl = "Exemples Biens - SCI SA.csv"

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

        els = {'numero': ('id', "numeroVoie", numero_voie),
               'voie': ('name', "nomVoie", nom_voie),
               'ville': ('id', "ville", nom_ville),
               'code_postal': ('id', "codePostal", code_postal)}
        last_el = None
        for el in els.keys():
            el_info = els[el]
            if el_info[0] == 'name':
                form = driver.find_element_by_name(el_info[1])
            elif el_info[0] == 'id':
                form = driver.find_element_by_id(el_info[1])

            form.click()
            form.clear()
            form.send_keys(el_info[2])

            last_el = form
        form.send_keys(Keys.ENTER)


# demo
api = CadastreAPI()
liste_bien = api.liste_biens()
#print(liste_bien.iloc[0])
print(liste_bien)
api.scraping("98", "av kleber", "paris 16", "75016")
#api.scraping(numero_voie= [0], nom_voie= [1], nom_ville= [2], code_postal=[3])