import time

from appium import webdriver

from start_session import start_session_test
from report_contagion import report_contagion_test

def start_session_and_report_contagion_test(driver):
    start_session_test(driver)
    report_contagion_test(driver)

if __name__ == "__main__":
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 15 seconds because of the initial informative image of the app
    time.sleep(15)

    start_session_and_report_contagion_test(driver)