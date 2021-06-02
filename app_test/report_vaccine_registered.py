import time

from appium import webdriver

from report_vaccine import report_vaccine_test
from start_session import start_session_test


def report_contagion_registered_test(driver):
    start_session_test(driver)
    time.sleep(2)
    report_vaccine_test(driver)


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

    report_contagion_registered_test(driver)
