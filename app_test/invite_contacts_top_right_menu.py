import time

from appium import webdriver

from invite import invite_test

def invite_contacts_test(driver):
    time.sleep(3)
    topRightMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
    topRightMenu.click()
    invite_contacts_option = driver.find_element_by_accessibility_id("Invita a tus contactos")
    invite_contacts_option.click()
    invite_test(driver)

if __name__ == '__main__':
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 10 seconds because of the initial informative image of the app
    time.sleep(10)
    
    # From login screen to invite your contacts screen
    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    continueWithoutRegister.click()

    invite_contacts_test(driver)
