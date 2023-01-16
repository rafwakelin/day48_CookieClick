from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import time

chrome_driver_path = "/Users/rafaelqueiroz/Desktop/chromedriver"
PRODUCT_URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome()
driver.get(PRODUCT_URL)

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

game_on = True

while game_on:
    try:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()

        if time.time() > timeout:
            money = driver.find_element(By.ID, "money")
            money_list = money.text.split(",")
            total_money = int("".join(money_list))

            time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
            time_machine_price = time_machine.text.split(sep="-")[1]
            time_machine_price_list = time_machine_price.split(sep=",")
            time_machine_price_final = int("".join(time_machine_price_list))

            portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
            portal_price = portal.text.split(sep="-")[1]
            portal_price_list = portal_price.split(sep=",")
            portal_price_final = int("".join(portal_price_list))

            lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
            lab_price = lab.text.split(sep="-")[1]
            lab_price_list = lab_price.split(sep=",")
            lab_price_final = int("".join(lab_price_list))

            ship = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
            ship_price = ship.text.split(sep="-")[1]
            ship_price_list = ship_price.split(sep=",")
            ship_price_final = int("".join(ship_price_list))

            mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
            mine_price = mine.text.split(sep="-")[1]
            mine_price_list = mine_price.split(sep=",")
            mine_price_final = int("".join(mine_price_list))

            factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
            factory_price = factory.text.split(sep="-")[1]
            factory_price_list = factory_price.split(sep=",")
            factory_price_final = int("".join(factory_price_list))

            grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
            grandma_price = grandma.text.split(sep="-")[1]
            grandma_price_list = grandma_price.split(sep=",")
            grandma_price_final = int("".join(grandma_price_list))

            hand = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
            hand_price = hand.text.split(sep="-")[1]
            hand_price_list = hand_price.split(sep=",")
            hand_price_final = int("".join(hand_price_list))

            if total_money >= time_machine_price_final:
                time_machine.click()
                print("Bought a time machine")

            elif total_money >= portal_price_final:
                portal.click()
                print("Bought a portal")

            elif total_money >= lab_price_final:
                lab.click()
                print("Bought a lab")

            elif total_money >= ship_price_final:
                ship.click()
                print("Bought a ship")

            elif total_money >= mine_price_final:
                mine.click()
                print("Bought a mine")

            elif total_money >= factory_price_final:
                factory.click()
                print("Bought a factory")

            elif total_money >= grandma_price_final:
                grandma.click()
                print("Bought a grannie")

            elif total_money >= hand_price_final:
                hand.click()
                print("Bought a hand")

            else:
                cookie.click()

    except StaleElementReferenceException:
        continue

if time.time() > five_min:
    cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cps"]')
    print(cookies_per_second.text)

driver.close()
