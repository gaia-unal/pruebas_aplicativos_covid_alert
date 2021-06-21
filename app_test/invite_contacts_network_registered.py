import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from start_session import start_session_test

from invite import invite_test


def invite_contacts_network_registered_test(driver):
    start_session_test(driver)
    time.sleep(2)
    red = driver.find_element_by_accessibility_id(
        "Mi red de contactos\nPestaña 3 de 5")
    red.click()
    time.sleep(2)

    for i in range(7):
        time.sleep(1)
        TouchAction(driver)   .press(x=362, y=398)   .move_to(
            x=362, y=130)   .release()   .perform()

    time.sleep(3)
    button_share = driver.find_element_by_accessibility_id("Compártela")
    button_share.click()
    invite_test(driver)


if __name__ == '__main__':
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "9"
    caps["deviceName"] = "j4primelte"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 10 seconds because of the initial informative image of the app
    time.sleep(10)

    invite_contacts_network_registered_test(driver)
