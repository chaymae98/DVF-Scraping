import select

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# selenium permet de lancer un navigateur web
driver = webdriver.Chrome()
print(type(driver))

# ouvrir la page web
url = "https://app.dvf.etalab.gouv.fr/"
print("lancement navigateur")
driver.get(url)

"""element = driver.find_element_by_name("departements")
drp=Select(element)
drp.select_by_index(3)
"""


numero_departement = driver.find_elements_by_name("departements").send_keys('01 - Ain')
"""numero_departement.click()
numero_departement.clear()
numero_departement.send_keys()
"""


"""nom_commune = driver.find_element_by_id("communes")
nom_commune.click()
nom_commune.clear()
nom_commune.send_keys("paris")
"""






