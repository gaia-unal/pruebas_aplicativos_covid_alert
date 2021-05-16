
from appium import webdriver
import time

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

#Definitions of name of elements of CovidAlert
home = driver.find_element_by_accessibility_id("Inicio\nTab 1 of 5")
contagions = driver.find_element_by_accessibility_id("Contagios por comunas y días\nTab 2 of 5")
red = driver.find_element_by_accessibility_id("Mi red de contactos\nTab 3 of 5")
reportCovid = driver.find_element_by_accessibility_id("Reportar contagio Covid\nTab 4 of 5")
reportVaccine = driver.find_element_by_accessibility_id("Reportar vacuna\nTab 5 of 5")

time.sleep(3)
#First button ("inicio"):
home.click()

time.sleep(3) #This time is recommended for helping the right develop of processes
#Second: contagions by communes
contagions.click()

time.sleep(3)
#Third: My red od contacts
red.click()

time.sleep(3)
#Fourth: report covid infection
reportCovid.click()

time.sleep(3)
#Fifth: report vaccine
reportVaccine.click()


