from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


def login(account_mail, account_password):

    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    # Login page
    driver.get("https://www.solotodo.cl/account/login")

    # Credentials
    mail = driver.find_element(
        by=By.XPATH, value='//*[@id="exampleInputEmail1"]').send_keys(account_mail)
    password = driver.find_element(
        by=By.XPATH, value='//*[@id="password"]').send_keys(account_password)
    signin = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input').click()
    print("\n")
    print("########################################################")
    print("\n")
    print("                  Login successful")
    print("\n")
    print("########################################################")
    print("\n")
    time.sleep(300)

    return 0


print("\n")
print("########################################################")
print("\n")
print("          Login automation in www.solotodo.cl")
print("\n")
print("########################################################")
print("\n")
print("Do you want to use the 'credentials.txt' file?")

while 1:
    option = input("y(yes) / n(no) / e(exit): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    if(option == "y"):
        print("\n")
        print("########################################################")
        print("\n")
        print("                   Automated login")
        print("\n")
        print("########################################################")
        print("\n")
        credentials = open("credentials.txt", "r")
        mail = credentials.readlines(1)[0]
        password = credentials.readlines(2)[0]
        login(mail, password)
        break
    elif(option == "n"):
        print("\n")
        print("########################################################")
        print("\n")
        print("                   Manual login")
        print("\n")
        print("########################################################")
        print("\n")
        mail = input("Please enter the mail: ")
        password = input("Please enter the Password: ")
        login(mail, password)
        break
    elif(option == "e"):
        print("\n")
        print("########################################################")
        print("\n")
        print("                      Bye bye!")
        print("\n")
        print("########################################################")
        print("\n")
        break
    else:
        print("Option not supported, try again! \n")
