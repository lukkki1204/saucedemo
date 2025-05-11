from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):
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