from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r'/Users/tanaloysius/Development/chromedriver')
driver = webdriver.Chrome(service=Service(r"/Users/tanaloysius/Development/chromedriver"))

driver.get('https://en.wikipedia.org/wiki/Main_Page')
articleCount = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(articleCount.text)

driver.quit()