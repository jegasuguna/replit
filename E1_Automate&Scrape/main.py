from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


service=Service("/Users/jegasuguna/Downloads/chromedriver-mac-x64//chromedriver")

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  output=float(text.split(": ")[1])
  return output

def write_files(text):
    filename= f"{dt.now().strftime('%Y-%m-%d.%H-%M')}.txt"
    #to create a new file
    with open(filename, 'w') as file:
        file.write(text)

def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated") 
  # driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+ Keys.RETURN) to press enter
  driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[3]/form/button").click()
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  text= str( clean_text(element.text))
  write_files(text)


print(main())