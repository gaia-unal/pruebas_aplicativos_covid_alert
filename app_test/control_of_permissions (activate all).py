import time

from appium import webdriver


def control_of_permission_activate_all_test(driver):    

    #1 definition:
    bars = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
    
    #Click in bars
    time.sleep(2)
    bars.click()
    time.sleep(2)

    #Click in control of permissions
    time.sleep(2)
    control = driver.find_element_by_accessibility_id(
        "Control de permisos")
    control.click()
    time.sleep(3)

    #definitions inside control permissions (can currently be seen on the screen)
    gps = driver.find_element_by_xpath(
        "(//android.view.View[@content-desc=\"Off\"])[1]")
    camera = driver.find_element_by_xpath(
        "(//android.view.View[@content-desc=\"Off\"])[2]")
    iotDevice = driver.find_element_by_xpath(
        "(//android.view.View[@content-desc=\"Off\"])[3]")
    

    #Click in activate GPS
    time.sleep(2)
    gps.click()

    #Click in activate Camera
    time.sleep(2)
    camera.click()

    #Click in activate IOT device
    time.sleep(2)
    iotDevice.click()

    from appium.webdriver.common.touch_action import TouchAction
    TouchAction(driver)   .press(x=292, y=1365)   .move_to(x=338, y=643)   .release()   .perform()

    time.sleep(3)

    #On the screen can see now, the options: Help to improve the system and near Contacts, for this here are the definitions
    system = driver.find_element_by_xpath(
        "(//android.view.View[@content-desc=\"Off\"])[1]") 
    nearContacts = driver.find_element_by_xpath(
        "(//android.view.View[@content-desc=\"Off\"])[2]")

    #Click in help to improve the system
    system.click()

    #Click in near contacts
    time.sleep(2)
    nearContacts.click()

    time.sleep(10)
    driver.back
    

if __name__ == '__main__':
    #this test works assuming that all permissions are turned off

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

    #Link that allow you enter to the app without a preview register
    withoutRegister = driver.find_element_by_accessibility_id("continuar sin registrarme")
    withoutRegister.click()

    time.sleep(3)

    control_of_permission_activate_all_test(driver)
