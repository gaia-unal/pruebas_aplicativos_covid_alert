import time

from appium import webdriver

from bottom_menu_navigation import bottom_menu_navigation_test
from start_session import start_session_test


def bottom_menu_navigation_registered_test(driver):

    start_session_test(driver)
    bottom_menu_navigation_test(driver)


if __name__ == '__main__':

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = '7'
    caps["deviceName"] = 'joan'
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Time needed to reach the "allow" button in the location permission window
    time.sleep(15)

    bottom_menu_navigation_registered_test(driver)
