import time

from appium import webdriver


def read_QR_test(driver):
    # From start menu to QR code reading screen
    qrCodeMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView")
    qrCodeMenu.click()
    time.sleep(3)
    allowCameraPermission = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_button")
    allowCameraPermission.click()

    # Once here, we should scan the code moving our cellphone


if __name__ == '__main__':
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

    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    continueWithoutRegister.click()
    time.sleep(3)

    read_QR_test(driver)
