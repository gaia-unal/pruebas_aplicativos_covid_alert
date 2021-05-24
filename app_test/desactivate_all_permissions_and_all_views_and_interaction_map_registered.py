import time

from appium import webdriver

from bottom_menu_navigation import bottom_menu_navigation_test
from control_of_permissions_desactivate_all import \
    control_of_permission_desactivate_all_test
from interaction_with_contagion_risk_map import \
    interaction_with_contagion_risk_map_test
from start_session import start_session_test
from top_right_menu import top_right_menu_test


def desactivate_all_permissions_and_all_views_map_registered_test(driver):

    start_session_test(driver)

    # Activate all permissions (It is assumed that all permissions are turned off)
    control_of_permission_desactivate_all_test(driver)
    driver.back()

    top_right_menu_test(driver)

    time.sleep(4)

    bottom_menu_navigation_test(driver)
    # The last view is: Contagions in communes

    interaction_with_contagion_risk_map_test(driver)


if __name__ == '__main__':

    nameTelephone = "j4primelte"
    versionAndroid = '9'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = 'true'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # Sleep for 15 seconds because of the initial informative image of the app
    time.sleep(15)

    desactivate_all_permissions_and_all_views_map_registered_test(driver)
