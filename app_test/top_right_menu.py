import time

from appium import webdriver


def top_right_menu_test(driver):

    topRightMenu.click()

    options = []

    permissionControl = driver.find_element_by_accessibility_id("Control de permisos")
    options.append(permissionControl)
    permissionControl.click()
    time.sleep(5)
    driver.back()

    # From start screen to invite your contacts screen
    inviteYourContacts = driver.find_element_by_accessibility_id("Invita a tus contactos")
    inviteYourContacts.click()
    options.append(inviteYourContacts)
    allowContactsAccess = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
    allowContactsAccess.click()
    # 10 seconds to let the app load the contact list and to see if the app shows the list correctly
    time.sleep(10)
    driver.back()

    #Waiting for the rest of options to be released


if __name__ == '__main__':
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"

    # Two options of the Top Right Menu working for the tests: "Control de Permisos" and "Invita a tus contactos". All the other options still doesn't work because the app developers haven't finished them and they are inaccessible.
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    # Sleep for 30 seconds because of the initial informative image of the app and to wait the app to ask location permissions and allow it
    time.sleep(30)

    allowLocationAccess = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    allowLocationAccess.click()

    # mapping
    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    topRightMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")

    # From login to permission control
    continueWithoutRegister.click()

    top_right_menu_test(driver)
