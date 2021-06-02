import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from continue_without_register import continue_without_register_test

def contagion_date(driver, contagionDate):
    time.sleep(2)
    contagionDate.click()
    time.sleep(2)
    contagionDateEdit = driver.find_element_by_accessibility_id("Switch to input")
    contagionDateEdit.click()
    time.sleep(2)
    contagionDateInput = driver.find_element_by_class_name("android.widget.EditText")
    contagionDateInput.clear()
    contagionDateInput.send_keys("05/15/2021")
    time.sleep(2)
    contagionDateOk = driver.find_element_by_accessibility_id("OK")
    contagionDateOk.click()

def test_date(driver, testDate):
    time.sleep(2)
    testDate.click()
    time.sleep(2)
    testDateEdit = driver.find_element_by_accessibility_id("Switch to input")
    testDateEdit.click()
    time.sleep(2)
    contagionDateInput = driver.find_element_by_class_name("android.widget.EditText")
    contagionDateInput.clear()
    contagionDateInput.send_keys("05/17/2021")
    time.sleep(2)
    contagionDateOk = driver.find_element_by_accessibility_id("OK")
    contagionDateOk.click()

def symptoms_date(driver, symptomsDate):
    time.sleep(2)
    symptomsDate.click()
    time.sleep(2)
    symptomsDateEdit = driver.find_element_by_accessibility_id("Switch to input")
    symptomsDateEdit.click()
    time.sleep(2)
    symptomsDateInput = driver.find_element_by_class_name("android.widget.EditText")
    symptomsDateInput.clear()
    symptomsDateInput.send_keys("05/16/2021")
    time.sleep(2)
    symptomsDateOk = driver.find_element_by_accessibility_id("OK")
    symptomsDateOk.click()


def report_contagion_test(driver):
    time.sleep(3)
    reportContagionScreen = driver.find_element_by_accessibility_id(
        "Reportar contagio Covid\nTab 4 of 5")
    reportContagionScreen.click()

    # Mapping
    time.sleep(2)
    testDate = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]")
    sympthomatic = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.RadioButton[1]")
    asympthomatic = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.RadioButton[2]")

    #symptomatic test
    test_date(driver, testDate)
    sympthomatic.click()
    time.sleep(2)
    symptomsDate = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[7]")
    symptoms_date(driver, symptomsDate)
    time.sleep(2)
    report = driver.find_element_by_accessibility_id("Reportar")
    report.click()

    #asymptomatic test
    test_date(driver, testDate)
    asympthomatic.click()
    time.sleep(2)
    report = driver.find_element_by_accessibility_id("Reportar")
    report.click()



if __name__ == "__main__":
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
    report_contagion_test(driver)
