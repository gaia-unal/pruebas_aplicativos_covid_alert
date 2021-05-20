import time

from appium import webdriver

from start_session import start_session_test

from read_QR import read_QR_test


def read_QR_registered(driver):

    start_session_test(driver)
    read_QR_test(driver)


if __name__ == '__main__':

    nameTelephone = "j4primelte"
    versionAndroid = '9'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"]="UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"

    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

    #Time needed to reach the "allow" button in the location permission window 
    time.sleep(30)

    #Window about the allow of ubication, the selected option is: "allow"
    allowUbication = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #The last ID in other devices is: com.android.permissioncontroller:id/permission_allow_foreground_only_button
    allowUbication.click()
    time.sleep(3)

    read_QR_registered(driver)