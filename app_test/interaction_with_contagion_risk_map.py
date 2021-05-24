import datetime
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def ascending_order(driver, list1):

    time.sleep(2)
    # Start of the bar
    a = driver.find_element_by_accessibility_id(list1[0])
    # + 46 because is a good aproximmation in the coordinate, in general for the devices
    ubicationX = a.location.get('x') + 46

    # Obtein the width of the bar
    ancho = a.size.get("width")

    # The position in Y, on the bar
    # + 37 because is a good aproximmation in the coordinate, in general for the devices
    ubicationY = a.location.get('y') + 37

    # The first four points on the bar, have an advance of: 7%
    moveTo = ancho*(0.07)

    for i in range(3):
        time.sleep(3)
        TouchAction(driver)   .press(x=ubicationX + moveTo*i, y=ubicationY)   .move_to(
            x=ubicationX+moveTo*(i+1), y=ubicationY)   .release()   .perform()

    # Here, on the bar, the advance is: 8% (3rd position on the bar, beginning from 0)
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*2, y=ubicationY)   .move_to(
        x=ubicationX+moveTo*2 + ancho*(0.08), y=ubicationY)   .release()   .perform()

    actual = ubicationX+moveTo*2 + ancho*(0.08)

    # Now, the advance is again: 7%
    for i in range(10):
        time.sleep(3)
        TouchAction(driver)   .press(x=actual + moveTo*i, y=ubicationY)   .move_to(
            x=actual + moveTo*(i+1), y=ubicationY)   .release()   .perform()


def descending_order(driver, list1):

    time.sleep(5)
    a = driver.find_element_by_accessibility_id(list1[14])

    # Obtein the initial position
    ubicationX = a.size.get("width")-46

    # Width of the bar
    ancho = a.size.get("width")

    # The position in Y, on the bar
    # + 37 because is a good aproximmation in the coordinate, in general for the devices
    ubicationY = a.location.get('y') + 37

    # The first four points on the bar, have an advance of: 7%
    moveTo = ancho*(0.07)

    for i in range(3):
        time.sleep(3)
        TouchAction(driver)   .press(x=ubicationX - moveTo*i, y=ubicationY)   .move_to(
            x=ubicationX - moveTo*(i+1), y=ubicationY)   .release()   .perform()

    # Here, on the bar, the advance is: 8% (3rd position on the bar, beginning from 0 and from the last position of the bar)
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX - moveTo*3, y=ubicationY)   .move_to(
        x=ubicationX - moveTo*3 - ancho*(0.06), y=ubicationY)   .release()   .perform()

    actual = ubicationX - moveTo*3 - ancho*(0.06)
    for i in range(3):
        time.sleep(3)
        if(i == 1):
            actual = ubicationX - moveTo*3 - ancho*(0.05)
        elif(i == 2):
            actual = ubicationX - moveTo*3 - ancho*(0.04)
        else:
            actual = ubicationX - moveTo*3 - ancho*(0.06)
        TouchAction(driver)   .press(x=actual - moveTo*i, y=ubicationY)   .move_to(
            x=actual - moveTo*(i+1), y=ubicationY)   .release()   .perform()

    time.sleep(3)
    actual = ubicationX - moveTo*3 - ancho*(0.04)
    TouchAction(driver)   .press(x=actual - moveTo*3, y=ubicationY)   .move_to(
        x=actual - moveTo*3 - ancho*(0.06), y=ubicationY)   .release()   .perform()

    now = ubicationX - moveTo*3 - ancho*(0.04)
    for i in range(6):
        time.sleep(3)
        if(i == 4):
            actual = now - moveTo*3 - ancho*(0.03)
        else:
            actual = now - moveTo*3 - ancho*(0.04)
        TouchAction(driver)   .press(x=actual - moveTo*i, y=ubicationY)   .move_to(
            x=actual - moveTo*(i+1), y=ubicationY)   .release()   .perform()


def disorder(driver, list1):
    time.sleep(5)
    # Start of the bar
    a = driver.find_element_by_accessibility_id(list1[0])
    # + 46 because is a good aproximmation in the coordinate, in general for the devices
    ubicationX = a.location.get('x') + 46

    # Obtein the width of the bar
    ancho = a.size.get("width")

    # The position in Y, on the bar
    # + 37 because is a good aproximmation in the coordinate, in general for the devices
    ubicationY = a.location.get('y') + 37

    # The first four points on the bar, have an advance of: 7%
    moveTo = ancho*(0.07)

    # Movements:
    time.sleep(2)
    TouchAction(driver)   .press(x=ubicationX + moveTo, y=ubicationY)   .move_to(
        x=ubicationX+moveTo*4, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*4 + moveTo, y=ubicationY)   .move_to(
        x=ubicationX + moveTo, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo, y=ubicationY)   .move_to(
        x=ubicationX + moveTo*13, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*13, y=ubicationY)   .move_to(
        x=ubicationX + moveTo*13 - moveTo*7, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*14 - moveTo*7, y=ubicationY)   .move_to(
        x=ubicationX + moveTo*10, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*10, y=ubicationY)   .move_to(
        x=ubicationX + moveTo*12, y=ubicationY)   .release()   .perform()
    time.sleep(3)
    TouchAction(driver)   .press(x=ubicationX + moveTo*12, y=ubicationY)   .move_to(
        x=ubicationX + moveTo*12 - moveTo*3, y=ubicationY)   .release()   .perform()


def interaction_with_contagion_risk_map_test(driver):

    # First, click on: "Contagios por comunas y..."
    contagions = driver.find_element_by_accessibility_id(
        "Contagios por comunas y días\nTab 2 of 5")
    contagions.click()

    time.sleep(2)
    # Find the current date with Python
    today = datetime.date.today()
    today.ctime()
    tt = today.timetuple()

    day_ = tt.tm_mday
    month_ = tt.tm_mon

    print("Current date:")
    print(tt.tm_mday)
    print(tt.tm_mon)

    # List with the percentages of progress in the bar
    list1 = ["0%", "7%", "14%", "21%", "29%", "36%", "43%",
             "50%", "57%", "64%", "71%", "79%", "86%", "93%", "100%"]

    for i in range(len(list1)):

        if month_ < 10:
            list1[i] = list1[i] + ', ' + str(day_) + '/' + '0' + str(month_)
        else:
            list1[i] = list1[i] + ', ' + str(day_) + '/' + str(month_)
        ayer = today - datetime.timedelta(days=i+1)
        tt = ayer.timetuple()
        day_ = tt.tm_mday
        month_ = tt.tm_mon
    # Here, we have the accebilities id, of each point on the bar

    time.sleep(3)
    # Run in ascending order
    print("Ascending order")
    ascending_order(driver, list1)

    time.sleep(3)
    # Run in descending order
    print("Descending order")
    descending_order(driver, list1)

    time.sleep(3)
    # Run in desorder
    print("Disorder")
    disorder(driver, list1)


if __name__ == '__main__':

    nameTelephone = "joan"
    versionAndroid = '7'

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = versionAndroid
    caps["deviceName"] = nameTelephone
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.example.aprendiendo"
    caps["appActivity"] = ".MainActivity"
    caps["autoGrantPermissions"] = 'true'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    time.sleep(18)

    # Link that allow you enter to the app without a preview register
    withoutRegister = driver.find_element_by_accessibility_id(
        "continuar sin registrarme")
    withoutRegister.click()
    time.sleep(3)
    interaction_with_contagion_risk_map_test(driver)
