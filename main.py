from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from login import do_login
from invoice import do_invoice
from reports import get_invoiced_amount
from actions.combobox import select_combo_value
from actions.button import click_by_class
from actions.button import click_by_x_path
from actions.input import write_by_id

from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Firefox()
amount = 19000

do_login(driver)
#do_invoice(driver, amount)
get_invoiced_amount(driver)