import time

from appium import webdriver

from start_session import start_session_test

def close_session_test(driver):
    time.sleep(2)
    top_right_menu = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
    top_right_menu.click()
    time.sleep(2)
    close_session_button = driver.find_element_by_accessibility_id("Cerrar sesion")
    close_session_button.click()
    close_session_button.click()


if __name__ == '__main__':

    nameTelephone = "ginkgo"
    versionAndroid = '10'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Time needed to reach the "allow" button in the location permission window
    time.sleep(15)
    start_session_test(driver)
    close_session_test(driver)