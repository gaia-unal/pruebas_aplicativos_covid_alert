import time

from appium import webdriver

from start_session import start_session_test

from control_of_permissions_activate_all import control_of_permission_activate_all_test


def control_of_permissions_activate_all_registered_test(driver):

    start_session_test(driver)
    control_of_permission_activate_all_test(driver)


if __name__ == '__main__':
    # this test works assuming that all permissions are turned off

    nameTelephone = "j4primelte"
    versionAndroid = '9'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Time needed to reach the "allow" button in the location permission window
    time.sleep(30)

    # Window about the allow of ubication, the selected option is: "allow"
    allowUbication = driver.find_element_by_id(
        "com.android.packageinstaller:id/permission_allow_button")
    # The last ID in other devices is: com.android.permissioncontroller:id/permission_allow_foreground_only_button
    allowUbication.click()

    # Link that allow you enter to the app without a preview register
    withoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    withoutRegister.click()

    time.sleep(3)

    control_of_permissions_activate_all_registered_test(driver)
