from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def createAccount(account_name, account_password):
    driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)

    # Register
    driver.get("https://www.pccomponentes.com/signup")

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
    name = driver.find_element(
        by=By.XPATH, value='//*[@id="name"]').send_keys(account_name)
    mail = driver.find_element(
        by=By.XPATH, value='//*[@id="email"]').send_keys(Keys.CONTROL + "v")
    final_mail = driver.find_element(
        by=By.XPATH, value='//*[@id="email"]').get_attribute('value')

    password = driver.find_element(
        by=By.XPATH, value='//*[@id="password"]').send_keys(account_password)
    repeat_password = driver.find_element(
        by=By.XPATH, value='//*[@id="repeatPassword"]').click()
    repeat_password = driver.find_element(
        by=By.XPATH, value='//*[@id="repeatPassword"]').send_keys(account_password)

    privacy_policy = driver.find_element(
        by=By.XPATH, value='//*[@id="policy"]').click()

    discounts = driver.find_element(
        by=By.XPATH, value='//*[@id="newsletter"]').click()

    register = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/main/section[2]/form/button[2]').click()

    # Save the credentials in a txt file
    credentials = [final_mail, account_password]
    credentials_file = open("credentials.txt", "w")
    for c in credentials:
        credentials_file.write(c + "\n")
    credentials_file.close()
    print("\n")
    print("########################################################")
    print("\n")
    print("Account signup successful")
    print("\n")
    print("########################################################")
    print("\n")
    print("E-mail: " + credentials[0])
    print("password: " + credentials[1])

    time.sleep(10000)


print("\n")
print("########################################################")
print("\n")
print("Signup automation in www.pccomponentes.com")
print("\n")
print("########################################################")
print("\n")
print("The e-mail account will be generated in a fakemail website and the credentials will be stored in a new generated file called 'credentials.txt'")
print("\n")
name = input("Enter the name you want to use for the account: ")
password = input(
    "Enter the password you want to use for the generated account (Remember to use capital letters and numbers): ")
print("\n")
createAccount(name, password)
