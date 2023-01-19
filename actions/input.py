from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def write_by_id(driver, id, value):
    driver.find_element(By.ID, id).send_keys(value)
    