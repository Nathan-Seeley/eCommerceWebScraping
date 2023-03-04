from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import csv

file = open("computers_laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["name", "price","specifications", "number of reviews"])

browser_driver = Service(r"C:\Users\Owner\Desktop\devCodeCamp projects\Week 17 Web Scraping in Selenium\eCommerce-Project\eCommerceWebScraping\chromedriver.exe")
scraper = webdriver.Chrome(service=browser_driver)
# scraper = webdriver.ChromeOptions(options=browser_driver)

scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

scraper.find_element(By.ID, "closeCookieBanner").click()

unique_id = 1
while True: 
    computers = scraper.find_elements (By.CLASS_NAME, "pull-right price")
    for computer in computers:
        name = computer.find_element(By.CLASS_NAME, "title")
        price = computer.find_element(By.CLASS_NAME, "pull-right price")
        specifications = computer.find_element(By.CLASS_NAME, "description")
        number_of_reviews = computer.find_element(By.CLASS_NAME, "pull-right")[0]
        writer.writerow(
            [unique_id, name.text, price.text, specifications.text, number_of_reviews])
        unique_id += 1

    try:
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, "Next")
        element.click()
    except NoSuchElementException:
        break
file.close()
scraper.quit()