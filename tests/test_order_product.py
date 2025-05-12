from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

def test_correct_credentials(driver, login, cart):  
    # Put credentials for first name, last name and postal code
    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Lukasz")
    last_name.send_keys("Lukasz")
    postal_code.send_keys("12-345")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    summary = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "summary_info_label"))
    )

    assert "Payment Information:" in summary.text

def test_incorect_credentials_no_first_name(driver, login, cart):
    # Put credentials for first name, last name and postal code
    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    last_name.send_keys("Lukasz")
    postal_code.send_keys("12-345")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "error message not displayed"

def test_incorect_credentials_no_last_name(driver, login, cart):
    # Put credentials for first name, last name and postal code
    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Lukasz")
    postal_code.send_keys("12-345")
    
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "error message not displayed"

def test_incorect_credentials_no_postal_code(driver, login, cart):
    # Put credentials for first name, last name and postal code
    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Lukasz")
    last_name.send_keys("Lukasz")
    
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    error = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
    )

    assert error.is_displayed(), "error message not displayed"