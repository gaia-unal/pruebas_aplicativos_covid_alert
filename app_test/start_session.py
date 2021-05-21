import time

from appium import webdriver


def start_session_test(driver):
    cellphone = "3146587759"  # Change this string as you need

    userCellphoneTextBox = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
    userCellphoneTextBox.send_keys(
        cellphone)
    time.sleep(2)
    loginButton = driver.find_element_by_accessibility_id(
        "Ingresar")
    loginButton.click()
    # in this time the tester has to write manually the code received in the Cellphone
    time.sleep(20)


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

    start_session_test(driver)
