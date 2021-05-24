import time

from appium import webdriver

from bottom_menu_navigation import bottom_menu_navigation_test
from control_of_permissions_activate_all import \
    control_of_permission_activate_all_test
from top_right_menu import top_right_menu_test


def activate_all_permissions_and_all_views_test(driver):

    # Activate all permissions (It is assumed that all permissions are turned off)
    control_of_permission_activate_all_test(driver)
    driver.back()
    driver.back()

    top_right_menu_test(driver)

    time.sleep(5)

    bottom_menu_navigation_test(driver)


if __name__ == '__main__':

    nameTelephone = "j4primelte"
    versionAndroid = '9'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = 'true'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 15 seconds because of the initial informative image of the app
    time.sleep(15)

    # Link that allow you enter to the app without a preview register
    withoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    withoutRegister.click()
    time.sleep(3)

    activate_all_permissions_and_all_views_test(driver)
