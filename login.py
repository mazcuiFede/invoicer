from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def do_login(driver):
    cuil = os.getenv('CUIL')
    password = os.getenv('PASSWORD')
    driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml?action=SYSTEM&system=rcel")

    elem = driver.find_element(By.NAME, "F1:username")
    elem.send_keys(cuil)
    elem.send_keys(Keys.RETURN)

    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "F1:password")))

    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

