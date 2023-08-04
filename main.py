from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login import do_login
from invoice import do_invoice
from reports import get_invoiced_amount
from random import randrange
import time, math, random

from dotenv import load_dotenv
load_dotenv()

#quantity = 1

amounts = [2000,3000]

#i = 0
for amount in amounts:
    #ammount generated under Benford's law
    #amount = math.floor(10**random.random()) * 1000
    print("Generating invoice: $" + str(amount))
    driver = webdriver.Firefox()
    do_login(driver)
    do_invoice(driver, amount)
    driver.close()

    timer = randrange(3)
    print("Waiting for " + str(timer) + "secs.")
    time.sleep(timer)


driver = webdriver.Firefox()
do_login(driver)
get_invoiced_amount(driver)