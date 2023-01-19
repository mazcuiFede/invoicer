from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from actions.combobox import select_combo_value
from actions.button import click_by_class
from actions.button import click_by_x_path
from actions.input import write_by_id

def do_invoice(driver, amount):
    click_by_class(driver, 'btn_empresa')
    time.sleep(1)
    click_by_class(driver, 'ui-button-text')

    select_combo_value(driver, 'puntodeventa', '2')

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Continuar >']")


    select_combo_value(driver, 'idconcepto', '2')

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Continuar >']")

    select_combo_value(driver, 'idivareceptor', '5')
    click_by_x_path(driver, "//label[@for='formadepago1']")

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Continuar >']")


    write_by_id(driver, 'detalle_descripcion1', 'Servicios Informaticos')
    write_by_id(driver, 'detalle_precio1', amount)

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Continuar >']")

    time.sleep(1)
    click_by_x_path(driver, "//input[@value='Confirmar Datos...']")

