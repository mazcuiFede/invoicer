from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_by_class(driver, class_name):
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    elem.click()

def click_by_id(driver, id):
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id)))
    elem.click()

def click_by_x_path(driver, x_path):
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    elem.click()