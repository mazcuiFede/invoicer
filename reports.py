from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from actions.button import click_by_class
from actions.button import click_by_id
from actions.button import click_by_x_path

def get_invoiced_amount(driver):
    click_by_class(driver, 'btn_empresa')
    time.sleep(1)
    click_by_id(driver, 'btn_consultas')

    click_by_id(driver, 'fed_btn')
    click_by_x_path(driver, "//td[@class='button nav']")

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Buscar']")

    read_table(driver)

def read_table(driver):
    time.sleep(1)
    elements = driver.find_elements(By.XPATH, "//td[@title='Importe Total: Pesos Argentinos']")
    amount = 0
    for element in elements:
        amount = amount + float(element.text)
    
    print("Tu facturacion del ultimo año fue de " + "{0:,.2f}".format(amount))