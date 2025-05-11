from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time

def test_sort_options(driver: WebDriver, login):
    
    dropdown = Select(WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    ))
    dropdown.select_by_visible_text("Name (Z to A)")

    items1 = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_names1 = [item.text for item in items1]

    assert items_names1 == ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket", "Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light", "Sauce Labs Backpack"], "Not proper order Z to A."

    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Name (A to Z)")

    items2 = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_names2 = [item.text for item in items2]

    assert items_names2 == ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"], "Not proper order A to Z."

    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Price (low to high)")

    items3 = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_names3 = [item.text for item in items3]

    assert items3 == ["Sauce Labs Onesie", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Backpack", "Sauce Labs Fleece Jacket"], "Not proper order price low to high."
    

    
