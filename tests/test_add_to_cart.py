from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver, login):
    #driver.get("https://www.saucedemo.com/inventory.html")

    add = WebDriverWait(driver,2).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add.click()

    remove = WebDriverWait(driver,2).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )
    remove.click()

