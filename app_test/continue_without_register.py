import time

from appium import webdriver


def continue_without_register_test(driver):
    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    continueWithoutRegister.click()
    time.sleep(3)


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

    # Sleep for 15 seconds because of the initial informative image of the app 
    time.sleep(15)

    continue_without_register_test(driver)
