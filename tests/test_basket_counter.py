from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_basket_counter(driver, login):

    add1 = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add1.click()

    basket_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert basket_counter.text == "1", "First adding wrong"

    add2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add2.click()

    basket_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert basket_counter.text == "2", "Second adding wrong"

    remove1 = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    remove1.click()

    WebDriverWait(driver, 2).until(
        lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
    )

    basket_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert basket_counter.text == "1", "First removing wrong"

    remove2 = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    remove2.click()

    WebDriverWait(driver, 2).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
