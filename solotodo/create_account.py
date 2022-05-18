from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def createAccount(account_password):
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

    # Copy the mail from the mailgen
    fake_mail = driver.find_element(
        by=By.XPATH, value='//*[@id="copy-button"]').click()

    # Go to the solotodo tab
    driver.switch_to.window(driver.window_handles[0])

    # Enter the credentials
    mail = driver.find_element(
        by=By.ID, value='inputEmail').send_keys(Keys.CONTROL + "v")
    final_mail = driver.find_element(
        by=By.ID, value='inputEmail').get_attribute('value')

    password = driver.find_element(
        by=By.ID, value='inputPassword1').send_keys(account_password)
    repeat_password = driver.find_element(
        by=By.ID, value='inputPassword2').send_keys(account_password)

    register = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input').click()

    # Account confirmation
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(20)

    # The mail is inside an Iframe tag and Selenium needs to make a change in order to find elements inside
    driver.switch_to.frame('emailFrame')

    time.sleep(10)
    confirmation = driver.find_element(
        by=By.XPATH, value='/html/body/div/div[3]/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/a')
    actions = ActionChains(driver)

    # Open the url of the mail confirmation button in a new tab.
    actions.key_down(Keys.LEFT_CONTROL).click(confirmation).perform()

    # Go to that tab
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[2])

    # Save the credentials in a txt file
    credentials = [final_mail, account_password]
    credentials_file = open("credentials.txt", "w")
    for c in credentials:
        credentials_file.write(c + "\n")
    credentials_file.close()
    print("########################################################")
    print("Account signup successful")
    print("########################################################")
    print("\n")
    print("E-mail: " + credentials[0])
    print("password: " + credentials[1])

    time.sleep(10000)


print("\n")
print("########################################################")
print("Signup automation in www.solotodo.cl")
print("########################################################")
print("\n")
print("The e-mail account will be generated in a fakemail website and the credentials will be stored in a new generated file called 'credentials.txt'")
print("\n")
password = input(
    "Enter the password you want to use for the generated account (Remember to use capital letters and numbers): ")
print("\n")
createAccount(password)
