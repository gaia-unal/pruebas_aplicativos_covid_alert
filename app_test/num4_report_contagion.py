import time

from appium import webdriver

from continue_without_register import continue_without_register_test


def report_contagion_test(driver):
    reportContagionScreen = driver.find_element_by_accessibility_id(
        "Reportar contagio Covid\nTab 4 of 5")
    reportContagionScreen.click()


if __name__ == "__main__":
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 30 seconds because of the initial informative image of the app and to wait the app to ask location permissions and allow it
    time.sleep(30)
    allowLocationAccess = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    allowLocationAccess.click()
    time.sleep(3)
    continue_without_register_test(driver)
