import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selenium permet de lancer un navigateur web
driver = webdriver.Chrome()
print(type(driver))

# ouvrir la page web
url = "https://www.cadastre.gouv.fr/scpc/accueil.do"
print("lancement navigateur")
driver.get(url)

numero_voie = driver.find_element_by_id("numeroVoie")
numero_voie.click()
numero_voie.clear()
numero_voie.send_keys("45")

nom_voie = driver.find_element_by_name("nomVoie")
nom_voie.click()
nom_voie.clear()
nom_voie.send_keys("rue poncelet")

ville = driver.find_element_by_id("ville")
ville.click()
ville.clear()
ville.send_keys("")

code_postal = driver.find_element_by_id("codePostal")
code_postal.click()
code_postal.clear()
code_postal.send_keys("75017")

code_postal.send_keys(Keys.ENTER)
# driver.close()
