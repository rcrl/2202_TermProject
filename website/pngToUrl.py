#
from selenium import webdriver
from selenium.webdriver.common.by import By
#
import time
import clipboard

def getImageUrl_ifh():
    #
    url = "https://ifh.cc/"
    driver = webdriver.Chrome()
    driver.get(url)

    #
    fileSelector = driver.find_element( by= By.XPATH, value= "//*[@id='fileSelector']" )
    fileSelector.send_keys(r'C:\Users\USER\PycharmProjects\TermProject\wcloud.png')

    #
    upload = driver.find_element( by= By.XPATH, value= '//*[@id="uploadButton"]' )
    upload.click()

    #
    time.sleep(5)
    url = driver.find_element( by= By.XPATH, value= '//*[@id="MAIN"]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input' )
    url.click()

    #
    image_url = clipboard.paste()

    #
    print(__name__, time.asctime())

    return image_url

def getImageUrl_zpat():
    #
    url = "https://www.zpat.info/"
    driver = webdriver.Chrome()
    driver.get(url)

    #
    fileSelector = driver.find_element( by= By.XPATH, value= '/html/body/header/div/form/div/input' )
    fileSelector.send_keys(r'C:\Users\USER\PycharmProjects\TermProject\wcloud.png')

    #
    time.sleep(2)
    upload = driver.find_element( by=By.XPATH, value= '/html/body/header/div/form/div/button')
    upload.click()

    #
    time.sleep(5)
    upload = driver.find_element( by= By.XPATH, value= '//*[@id="ControlTextarea1"]' )

    #
    image_url = upload.text
    print(image_url)

    #
    print(__name__, time.asctime())

    return image_url

