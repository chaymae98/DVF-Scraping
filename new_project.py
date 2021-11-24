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
url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
print("lancement navigateur")
driver.get(url)

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)
drp.select_by_index(3)

print(drp)