import time

from appium import webdriver

def invite_test(driver):
    time.sleep(10)
    searchBox = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
    searchBox.send_keys("numPrueba")
    time.sleep(2)
    contact1 = driver.find_element_by_accessibility_id("NumPrueba")
    contact1.click()
    contact2 = driver.find_element_by_accessibility_id("NumPrueba2")
    contact2.click()
    driver.back()
    time.sleep(2)
    nextButton = driver.find_element_by_accessibility_id("Siguiente")
    nextButton.click()
    time.sleep(2)
    strongContact1 = driver.find_element_by_accessibility_id("NumPrueba")
    strongContact1.click()
    time.sleep(2)
    sendInvitationButton = driver.find_element_by_accessibility_id("Enviar")
    sendInvitationButton.click()