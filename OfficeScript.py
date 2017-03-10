#!/usr/bin/python3
# -*- coding: utf-8 -*-

#führt einen Login auf campussachsen.tu-dresden.de
#für einen Uni Leipzig Account aus um das Office Abo zu verlängern

#zur Eingabe der Logindaten von Konsole/Terminal aufrufen
#ggf an geeignetem Ort (z.B./usr/local/bin/) speichern und zum Autostart hinzufügen
#Logindaten löschen über Parameteraufruf "-deleteLogin"

#geckodriver muss im PATH sein
#https://github.com/mozilla/geckodriver/releases
#kopieren nach /usr/local/bin


import sys
import time
import getpass
import keyring #pip install -U keyring
from selenium import webdriver #pip install -U selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

if(len(sys.argv) > 1 and sys.argv[1] == "-deleteLogin"):
  print("Lösche login daten")
  if(not keyring.get_password("CampussachsenOffice", "username") is None):
    keyring.delete_password("CampussachsenOffice", "username")
  if(not keyring.get_password("CampussachsenOffice", "password") is None):
    keyring.delete_password("CampussachsenOffice", "password")
  sys.exit(0)



username = keyring.get_password("CampussachsenOffice", "username")
if(username is None):
  username = input("Username nicht gefunden! Bitte Username eingeben:")
  keyring.set_password("CampussachsenOffice", "username", username)

password = keyring.get_password("CampussachsenOffice", "password")
if(password is None):
  password = getpass.getpass("Passwort nicht gefunden! Bitte Username eingeben:")
  keyring.set_password("CampussachsenOffice", "password", password)




driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://campussachsen.tu-dresden.de/o365/index.php")

#ggf. alert schließen
try:
  alert = driver.switch_to_alert()
  alert.accept()
except:
  pass
#login Button
driver.find_element_by_id("imput").click()
time.sleep(1)
#Uni Leipzig auswählen
select = Select(driver.find_element_by_xpath("//select"))
select.select_by_visible_text("Universität Leipzig")
driver.find_element_by_id("sub").click()
time.sleep(1)
#Username + Passwort
driver.find_element_by_name("j_username").send_keys(username)
driver.find_element_by_name("j_password").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
#Ablaufdatum auslesen
dateInfo = driver.find_element_by_xpath("//body").text.split("Ablaufdatum: ")[1].split("\n")[0]
print("Login aktualisiert. Neues Ablaufdatum: ", dateInfo)
#logout button
driver.find_element_by_id("imput").click()
time.sleep(1)
driver.quit()
