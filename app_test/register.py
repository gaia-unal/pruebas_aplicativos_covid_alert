import time

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction


def register_test(driver):
    
    #Click to URL: ¿No tienes cuenta? Regístrate
    register = driver.find_element_by_accessibility_id(
        "¿No tienes cuenta?Regístrate")
    register.click()
    time.sleep(5)
 
    #Click to: type of id: C.C, C.E or T.I
    typeId = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[1]")
    typeId.click()
    option = driver.find_element_by_accessibility_id(
        "C.C")    
    option.click()

    #Number of Id document
    document = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]")
    document.click()
    document.send_keys(
        "30298609")

    #scroll
    scroll1 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
    scroll1.click()


    date = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
    date.click()

    inputDate = driver.find_element_by_accessibility_id(
        "Switch to input")
    inputDate.click()

    textboxDate = driver.find_element_by_class_name(
        "android.widget.EditText")
    textboxDate.clear()

    textboxDate.send_keys(
        "08/12/2001")
    confirm = driver.find_element_by_accessibility_id(
        "OK")
    confirm.click()
    time.sleep(5) #Neccessary time to load

    
    space = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]")
    space.click()
    
    # Telephone number
    number = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]")
    number.send_keys(
        "3133302224")
    driver.back()
    time.sleep(3)

    TouchAction(driver)   .press(x=660, y=1654)   .move_to(x=675, y=324)   .release()   .perform()

    site = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[1]")
    site.click()
    time.sleep(2)

    #Commune of Manizales
    commune = driver.find_element_by_accessibility_id(
        "San JosÃ©")
    commune.click()
    time.sleep(5)

    #scroll2
    scroll2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[3]")
    scroll2.click()
    time.sleep(2)
    
    #neigh
    neigh = driver.find_element_by_accessibility_id(
        "Galan")
    neigh.click()
    time.sleep(2)
    
    #Final the button for register
    finalButton = driver.find_element_by_accessibility_id(
        "Registrarme")
    finalButton.click()
    

if __name__ == '__main__':
    
    nameTelephone="j4primelte"
    versionAndroid="9"

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"]="UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = "com.example.aprendiendo.MainActivity"
    
    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

    #Time needed to reach the "allow" button in the location permission window 
    time.sleep(30)

    #Window about the allow of ubication, the selected option is: "allow"
    allowUbication = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    allowUbication.click()
    time.sleep(5)

    register_test(driver)