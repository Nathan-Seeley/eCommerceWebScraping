from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import csv
file = open("computers_laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["name", "price","specifications", "number of reviews"])
browser_driver = Service("chromedriver.exe")
scraper = webdriver.Chrome(service=browser_driver)
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
scraper.find_element(By.CLASS_NAME, "acceptCookies").click()
# wait = WebDriverWait(scraper, 10)
# element_to_watch = scraper.find_element(By.CLASS_NAME,"col-md-9")
unique_id = 1
while True: 
    computers = scraper.find_elements (By.CLASS_NAME, "thumbnail")
    for computer in computers:
        name = computer.find_element(By.CLASS_NAME, "title").text
        price = computer.find_element(By.CLASS_NAME, "price").text
        specifications = computer.find_element(By.CLASS_NAME, "description").text
        # number_of_reviews = computer.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/*div[2]/div/div[2]/p[2]").get_attribute("data-rating")
        number_of_reviews = computer.find_element(By.XPATH,"//p[2]").get_attribute("data-rating")
        writer.writerow(
            [unique_id, name, price, specifications, number_of_reviews])
        unique_id += 1
    try:
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, "›")
        element.click()
    except NoSuchElementException:
        break
file.close()
scraper.quit()
