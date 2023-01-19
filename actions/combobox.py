from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def select_combo_value(driver, element_id, value):
    select = Select(driver.find_element(By.ID, element_id))

    # select by visible text
    select.select_by_value(value)
