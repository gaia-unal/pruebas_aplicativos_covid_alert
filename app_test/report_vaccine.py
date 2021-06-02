import time

from appium import webdriver

from continue_without_register import continue_without_register_test


def edit_a_date(driver, cadena):
    edit = driver.find_element_by_accessibility_id("Switch to input")
    edit.click()
    edit2 = driver.find_element_by_class_name("android.widget.EditText")
    edit2.clear()
    edit2.send_keys(cadena)
    fin1 = driver.find_element_by_accessibility_id("OK")
    fin1.click()


def enter_dates(driver):
    date_first_dose = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]")
    date_second_dose = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]")

    date_first_dose.click()
    cadena = "03/01/2021"
    edit_a_date(driver, cadena)
    time.sleep(2)

    date_second_dose.click()
    cadena = "06/01/2021"
    edit_a_date(driver, cadena)
    time.sleep(2)

    report = driver.find_element_by_accessibility_id("Reportar")
    report.click()


def report_vaccine_test(driver):
    time.sleep(2)
    vaccine = driver.find_element_by_accessibility_id(
        "Reportar vacuna\nTab 5 of 5")
    vaccine.click()
    time.sleep(2)
    marc = driver.find_element_by_accessibility_id("Marca de Vacuna")
    marc.click()
    typevaccine = driver.find_element_by_accessibility_id("AstraZeneca")
    typevaccine.click()
    enter_dates(driver)
    time.sleep(5)


if __name__ == "__main__":
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "7"
    caps["deviceName"] = "joan"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = "true"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 15 seconds because of the initial informative image of the app
    time.sleep(15)

    continue_without_register_test(driver)
    report_vaccine_test(driver)
