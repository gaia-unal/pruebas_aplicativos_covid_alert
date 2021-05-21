import time

from appium import webdriver


def invite_contacts_test(driver):

    # Ready to test the contact invitation with a test contact called "numPrueba"
    time.sleep(3)
    topRightMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
    topRightMenu.click()

    inviteYourContacts = driver.find_element_by_accessibility_id(
        "Invita a tus contactos")
    inviteYourContacts.click()
    allowContactsAccess = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_button")
    allowContactsAccess.click()
    # 10 seconds to let the app load the contact list and to see if the app shows the list correctly
    time.sleep(10)

    # Searching and inviting a contact called "numPrueba"
    searchContact = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText")
    searchContact.send_keys("numPrueba")
    time.sleep(3)
    sendInvitation = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"NumPrueba\n302 4350670\"]/android.widget.Button")
    sendInvitation.click()
    time.sleep(15)  # Time to wait for response of the action

    driver.back()  # This closes the keyboard
    driver.back()  # This returns to the top right menu
    driver.back()  # this returns to the main menu


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

    # From login screen to invite your contacts screen
    continueWithoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    continueWithoutRegister.click()

    invite_contacts_test(driver)
