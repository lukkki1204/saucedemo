from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_basket_content(driver, login):
    
    add1 = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add1.click()

    add2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add2.click()

    basket = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    basket.click()

    items = WebDriverWait(driver, 2).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )

    items_names = [item.text for item in items]

    assert "Sauce Labs Backpack" in items_names, "Backpack not detected"
    assert "Sauce Labs Bike Light" in items_names, "Bike light not detected"

    remove1 = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    remove1.click()

    remove2 = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    remove2.click()

    items2 = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    items_names2 = [item.text for item in items2]

    assert "Sauce Labs Backpack" not in items_names2, "Backpack still present in the basket"
    assert "Sauce Labs Bike Light" not in items_names2, "Bike light still present in the basket"