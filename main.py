from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login import do_login
from reports import get_invoiced_amount

from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Firefox()
amount = 19000

do_login(driver)
#do_invoice(driver, amount)
get_invoiced_amount(driver)