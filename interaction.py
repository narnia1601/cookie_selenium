from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import schedule
import time

service = Service(r'/Users/tanaloysius/Development/chromedriver')
driver = webdriver.Chrome(service=Service(r"/Users/tanaloysius/Development/chromedriver"))

driver.get('http://orteil.dashnet.org/experiments/cookie/')

def getMoney():
    money = driver.find_element(By.ID, 'money').text
    if ',' in money:
        money = money.replace(',', '')
    return int(money)

def getPrices():
    pricesDictionary = {}
    buyCursor = driver.find_element(By.ID, 'buyCursor')
    buyCursorPrice = buyCursor.text.split(' ')[2].split('\n')[0]
    if ',' in buyCursorPrice:
        buyCursorPrice = buyCursorPrice.replace(',','')
    buyCursorPrice = int(buyCursorPrice)
    pricesDictionary['buyCursor'] = buyCursorPrice

    buyGrandma = driver.find_element(By.ID, 'buyGrandma')
    buyGrandmaPrice = buyGrandma.text.split(' ')[2].split('\n')[0]
    if ',' in buyGrandmaPrice:
        buyGrandmaPrice = buyGrandmaPrice.replace(',','')
    buyGrandmaPrice = int(buyGrandmaPrice)
    pricesDictionary['buyGrandma'] = buyGrandmaPrice

    buyFactory = driver.find_element(By.ID, 'buyFactory')
    buyFactoryPrice = buyFactory.text.split(' ')[2].split('\n')[0]
    if ',' in buyFactoryPrice:
        buyFactoryPrice = buyFactoryPrice.replace(',', '')
    buyFactoryPrice = int(buyFactoryPrice)
    pricesDictionary['buyFactory'] = buyFactoryPrice

    buyMine = driver.find_element(By.ID, 'buyMine')
    buyMinePrice = buyMine.text.split(' ')[2].split('\n')[0]
    if ',' in buyMinePrice:
        buyMinePrice = buyMinePrice.replace(',', '')
    buyMinePrice = int(buyMinePrice)
    pricesDictionary['buyMine'] = buyMinePrice

    buyShipment = driver.find_element(By.ID, 'buyShipment')
    buyShipmentPrice = buyShipment.text.split(' ')[2].split('\n')[0]
    if ',' in buyShipmentPrice:
        buyShipmentPrice = buyShipmentPrice.replace(',','')
    buyShipmentPrice = int(buyShipmentPrice)
    pricesDictionary['buyShipment'] = buyShipmentPrice

    buyAlchemyLab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
    buyAlchemyLabPrice = buyAlchemyLab.text.split(' ')[3].split('\n')[0]
    if ',' in buyAlchemyLabPrice:
        buyAlchemyLabPrice = buyAlchemyLabPrice.replace(',','')
    buyAlchemyLabPrice = int(buyAlchemyLabPrice)
    pricesDictionary['buyAlchemy lab'] = buyAlchemyLabPrice

    buyPortal = driver.find_element(By.ID, 'buyPortal')
    buyPortalPrice = buyPortal.text.split(' ')[2].split('\n')[0]
    if ',' in buyPortalPrice:
        buyPortalPrice = buyPortalPrice.replace(',','')
    buyPortalPrice = int(buyPortalPrice)
    pricesDictionary['buyPortal'] = buyPortalPrice

    buyTimeMachine = driver.find_element(By.ID, 'buyTime machine')
    buyTimeMachinePrice = buyTimeMachine.text.split(' ')[3].split('\n')[0]
    if ',' in buyTimeMachinePrice:
        buyTimeMachinePrice = buyTimeMachinePrice.replace(',','')
    buyTimeMachinePrice = int(buyTimeMachinePrice)
    pricesDictionary['buyTime machine'] = buyTimeMachinePrice
    return pricesDictionary

def buyItems():
    money = getMoney()
    pricesDictionary = getPrices()
    selectedItem: str
    pricesList = []
    for item in pricesDictionary:
        if pricesDictionary[item] < money:
            pricesList.append(pricesDictionary[item])
    maxPrice = max(pricesList)
    for item, price in pricesDictionary.items():
        if maxPrice == price:
            selectedItem = item
    driver.find_element(By.ID, selectedItem).click()
    print(pricesDictionary)

schedule.every(15).seconds.do(buyItems)

while True:
    schedule.run_pending()
    driver.find_element(By.ID, 'cookie').click()
