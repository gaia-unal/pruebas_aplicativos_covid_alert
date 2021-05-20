import time

from appium import webdriver

from start_session import start_session_test
from control_of_permissions_desactivate_all import control_of_permission_desactivate_all_test

def desactivate_all_permissions_registered_test(driver):
    start_session_test(driver)
    control_of_permission_desactivate_all_test(driver)


if __name__ == "__main__":
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    
    #Sleep for 30 seconds because of the initial informative image of the app and to wait the app to ask location permissions and allow it
    time.sleep(30)
    allowLocationAccess = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    allowLocationAccess.click()
    desactivate_all_permissions_registered_test(driver)

    