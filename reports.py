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
    
    print("Categoría C: de los $ 1.557.443 actuales a $ 2.080.367 anuales o $ 173.363 por mes. ")
    print("Categoría D: de los $ 1.934.273,04 actuales a $ 2.583.720 anuales o $ 215.310 por mes.")
    print("Categoría E: de los $ 2.277.684 actuales a $ 3.042.435 anuales o $ 253.536 por mes.")
    print("Tu facturacion del ultimo año fue de " + "{0:,.2f}".format(amount))
    print("Tu facturacion del promedio mensual es de " + "{0:,.2f}".format(amount / 12))