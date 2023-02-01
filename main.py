from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login import do_login
from invoice import do_invoice
from reports import get_invoiced_amount
from random import randrange
import time

from dotenv import load_dotenv
load_dotenv()

amount = 7500
quantity = 7

i = 0
while (i < quantity):
    driver = webdriver.Firefox()
    do_login(driver)
    do_invoice(driver, amount)
    driver.close()
    i = i + 1

    timer = randrange(5)
    print(timer)
    time.sleep(timer)


driver = webdriver.Firefox()
do_login(driver)
get_invoiced_amount(driver)