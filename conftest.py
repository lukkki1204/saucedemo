import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "load-extension"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get("https://www.saucedemo.com/")

    login = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    passwd = driver.find_element(By.ID, "password")

    login.send_keys("standard_user")
    passwd.send_keys("secret_sauce")

    passwd.send_keys(Keys.RETURN)

    name = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

@pytest.fixture
def cart(driver, login):
    
    # Add one element to the cart
    add = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add.click()
    
    # Select cart icon
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    # Select checkout button
    checkout_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()
