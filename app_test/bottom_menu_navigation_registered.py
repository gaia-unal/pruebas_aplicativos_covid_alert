import time

import random

from appium import webdriver

from bottom_menu_navigation import bottom_menu_navigation_test

from bottom_menu_navigation import run_in_ascending_order

from bottom_menu_navigation import run_in_descending_order

from bottom_menu_navigation import run_in_random_order

from bottom_menu_navigation import run_in_desorder

from start_session import start_session_test


def bottom_menu_navigation_registered_test(driver):

    start_session_test(driver)
    bottom_menu_navigation_test(driver)


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

    bottom_menu_navigation_registered_test(driver)