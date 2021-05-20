import time

import random

from appium import webdriver


def run_in_ascending_order(lista):

    for i in range (len(lista)):
        time.sleep(3)
        lista[i].click()

    
def run_in_descending_order(lista):

    lista.reverse()
    for i in range (len(lista)):
        time.sleep(3)
        lista[i].click()

def run_in_random_order(lista):

    for i in range (len(lista)*2):
        element=random.choice(lista)
        time.sleep(2)
        element.click()

def run_in_desorder(home, contagions, red, reportCovid, reportVaccine):
    time.sleep(2)
    reportVaccine.click()
    time.sleep(2)
    home.click()
    time.sleep(2)
    reportCovid.click()
    time.sleep(2)
    reportVaccine.click()
    time.sleep(2)
    contagions.click()
    time.sleep(2)
    home.click()
    time.sleep(2)
    red.click()


def bottom_menu_navigation_test(driver):

    time.sleep(5)
    lista=[]
    #Definitions of name of elements of CovidAlert
    home = driver.find_element_by_accessibility_id(
        "Inicio\nTab 1 of 5")
    lista.append(home)

    contagions = driver.find_element_by_accessibility_id(
        "Contagios por comunas y días\nTab 2 of 5")
    lista.append(contagions)

    red = driver.find_element_by_accessibility_id(
        "Mi red de contactos\nTab 3 of 5")
    lista.append(red)

    reportCovid = driver.find_element_by_accessibility_id(
        "Reportar contagio Covid\nTab 4 of 5")
    lista.append(reportCovid)

    reportVaccine = driver.find_element_by_accessibility_id(
        "Reportar vacuna\nTab 5 of 5")
    lista.append(reportVaccine)

    run_in_ascending_order(lista)
    time.sleep(3)
    run_in_descending_order(lista)
    time.sleep(3)
    run_in_random_order(lista)
    time.sleep(3)
    run_in_desorder(home,contagions,red,reportCovid,reportVaccine)
    time.sleep(3)

if __name__ == '__main__':

    nameTelephone = "j4primelte"
    versionAndroid = '9'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"]="UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"

    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

    #Time needed to reach the "allow" button in the location permission window 
    time.sleep(30)

    #Window about the allow of ubication, the selected option is: "allow"
    allowUbication = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #The last ID in other devices is: com.android.permissioncontroller:id/permission_allow_foreground_only_button
    allowUbication.click()
    time.sleep(3)

    #Link that allow you enter to the app without a preview register
    withoutRegister = driver.find_element_by_accessibility_id("continuar sin registrarme")
    withoutRegister.click()
    time.sleep(3)

    bottom_menu_navigation_test(driver)
