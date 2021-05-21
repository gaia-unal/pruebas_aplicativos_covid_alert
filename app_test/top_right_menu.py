import time
import random

from appium import webdriver

# Every of these options allways returns to the main menu


def mapping_top_right_menu_options(driver, options, topRightMenu):
    topRightMenu.click()
    time.sleep(1)
    permissionControl = driver.find_element_by_accessibility_id(
        "Control de permisos")
    inviteYourContacts = driver.find_element_by_accessibility_id(
        "Invita a tus contactos")
    options.append(permissionControl)
    options.append(inviteYourContacts)
    driver.back()


def navigation_in_order(driver, options, topRightMenu):
    time.sleep(3)
    topRightMenu.click()
    for option in options:
        option.click()
        time.sleep(3)
        driver.back()
    driver.back()


def navigation_in_disorder(driver, options, topRightMenu):
    time.sleep(3)
    topRightMenu.click()
    options.reverse()
    for option in options:
        option.click()
        time.sleep(3)
        driver.back()
    options.reverse()
    driver.back()


def random_navigation(driver, options, topRightMenu):
    time.sleep(3)
    topRightMenu.click()
    for i in range(len(options)*2):
        option = random.choice(options)
        option.click()
        time.sleep(3)
        driver.back()
    driver.back()


def top_right_menu_test(driver):
    time.sleep(3)
    topRightMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")

    options = []
    mapping_top_right_menu_options(driver, options, topRightMenu)

    print("En orden")
    navigation_in_order(driver, options, topRightMenu)
    print("En desorden")
    navigation_in_disorder(driver, options, topRightMenu)
    print("Aleatorio")
    random_navigation(driver, options, topRightMenu)

    # Waiting for the rest of options to be released
    time.sleep(3)
    # driver.back() # Remind to always return to the main menu, not only to the top right menu view


if __name__ == '__main__':
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    # Two options of the Top Right Menu working for the tests: "Control de Permisos" and "Invita a tus contactos". All the other options still doesn't work because the app developers haven't finished them and they are inaccessible.
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    # Sleep for 30 seconds because of the initial informative image of the app and to wait the app to ask location permissions and allow it
    time.sleep(15)

    # mapping
    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")

    # From login to permission control
    continueWithoutRegister.click()

    top_right_menu_test(driver)
