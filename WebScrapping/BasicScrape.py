from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# create a Chrome driver instance
chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(r"C:\Users\ganesh.tukarul\AppData\Local\Programs\Python\chromedriver_mac_arm64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# define the URL to scrape
url = "https://www.nseindia.com/option-chain"

# load the webpage
driver.get(url)

# wait for the webpage to load
driver.implicitly_wait(10)

# print the title of the webpage
print(driver.title)

# close the Chrome driver instance
driver.quit()
