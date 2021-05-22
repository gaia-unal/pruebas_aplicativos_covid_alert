import time

from appium import webdriver

import top_right_menu
import bottom_menu_navigation
from start_session import start_session_test

def mapping_bottom_menu_buttons(driver, bottom_menu_list):
    home = driver.find_element_by_accessibility_id(
        "Inicio\nTab 1 of 5")
    bottom_menu_list.append(home)

    contagions = driver.find_element_by_accessibility_id(
        "Contagios por comunas y días\nTab 2 of 5")
    bottom_menu_list.append(contagions)

    red = driver.find_element_by_accessibility_id(
        "Mi red de contactos\nTab 3 of 5")
    bottom_menu_list.append(red)

    reportCovid = driver.find_element_by_accessibility_id(
        "Reportar contagio Covid\nTab 4 of 5")
    bottom_menu_list.append(reportCovid)

    reportVaccine = driver.find_element_by_accessibility_id(
        "Reportar vacuna\nTab 5 of 5")
    bottom_menu_list.append(reportVaccine)

def top_right_menu_plus_bottom_menu_test(driver):

    start_session_test(driver)

    # First, we should mapp all the available options of the top right menu
    topRightMenu = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
    trm_options = [] #trm stands for top right menu
    top_right_menu.mapping_top_right_menu_options(driver, trm_options, topRightMenu)

    # Then, we should mapp the bottom menu buttons
    bottom_menu_list = []
    mapping_bottom_menu_buttons(driver, bottom_menu_list)

    #Here we start the test running different functions combinated
    top_right_menu.navigation_in_disorder(driver, trm_options, topRightMenu)
    bottom_menu_navigation.run_in_ascending_order(bottom_menu_list)
    top_right_menu.navigation_in_order(driver, trm_options, topRightMenu)
    bottom_menu_navigation.run_in_random_order(bottom_menu_list)
    top_right_menu.random_navigation(driver, trm_options, topRightMenu)
    bottom_menu_navigation.run_in_descending_order(bottom_menu_list)



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

    top_right_menu_plus_bottom_menu_test(driver)