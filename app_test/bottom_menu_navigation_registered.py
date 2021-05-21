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
    caps["autoGrantPermissions"] = "true"

    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

    #Time needed to reach the "allow" button in the location permission window 
    time.sleep(15)

    bottom_menu_navigation_registered_test(driver)