from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


def test_login_positive(driver):
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

    assert "Products" in name.text 

def test_login_empty_login(driver):
    driver.get("https://www.saucedemo.com/")

    login = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    passwd = driver.find_element(By.ID, "password")

    passwd.send_keys("secret_sauce")

    passwd.send_keys(Keys.RETURN)

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "Error message not displayed"

def test_login_empty_password(driver):
    driver.get("https://www.saucedemo.com/")

    login = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    passwd = driver.find_element(By.ID, "password")

    login.send_keys("standard_user")

    passwd.send_keys(Keys.RETURN)

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "Error message not displayed"

def test_login_wrong_login(driver):
    driver.get("https://www.saucedemo.com/")

    login = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    passwd = driver.find_element(By.ID, "password")

    login.send_keys("standard")
    passwd.send_keys("secret_sauce")

    passwd.send_keys(Keys.RETURN)

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

def test_login_wrong_password(driver):
    driver.get("https://www.saucedemo.com/")

    login = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    passwd = driver.find_element(By.ID, "password")

    login.send_keys("standard_user")
    passwd.send_keys("secret")

    passwd.send_keys(Keys.RETURN)

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "Error message not displayed"

