from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def crearCuenta():
    driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)

    # Register
    driver.get("https://www.solotodo.cl/account/signup")

    # Enable tab switching
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[1])

    # Go to fake mail gen
    driver.get("http://www.fakemailgenerator.com/")

    time.sleep(3)

    fake_mail = driver.find_element(
        by=By.XPATH, value='//*[@id="copy-button"]').click()

    driver.switch_to.window(driver.window_handles[0])

    mail = driver.find_element_by_id(
        'inputEmail').send_keys(Keys.CONTROL + "v")
    password = driver.find_element_by_id(
        'inputPassword1').send_keys('QuieroPasarElRamo1')
    repeat_password = driver.find_element_by_id(
        'inputPassword2').send_keys('QuieroPasarElRamo1')

    register = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input').click()

    # Account confirmation
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(20)

    driver.switch_to.frame('emailFrame')
    print("emailFrame")
    time.sleep(10)
    confirmation = driver.find_element(
        by=By.XPATH, value='/html/body/div/div[3]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/a')
    actions = ActionChains(driver)

    actions.key_down(Keys.LEFT_CONTROL).click(confirmation).perform()

    print("casi al original")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[2])
    driver.switch_to.parent_frame()

    time.sleep(3000)

    # New window
    mail_signin = driver.find_element_by_id(
        'email').send_keys(Keys.CONTROL + "v")
    password_signin = driver.find_element_by_id(
        'password').send_keys('QuieroPasarElRamo1')
    signin = driver.find_element(
        by=By.XPATH, value='//*[@id="main-container"]/div/div/div[3]/div/form/input').click()

    time.sleep(10000)


# driver.quit()
crearCuentaSoloTodo()
