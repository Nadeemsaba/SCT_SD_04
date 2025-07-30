from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

search_term = input("🔍 Enter a product to search on Amazon: ")

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

csv_filename = f"{search_term.replace(' ', '_')}_products.csv"

with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Reviews", "Product URL", "Image URL"])  # Removed Rating

    for page in range(1, 4):  # Scrape first 3 pages
        driver.get(f"https://www.amazon.in/s?k={search_term}&page={page}")
        time.sleep(3)

        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for product in products:
            try:
                name = product.find_element(By.XPATH, './/h2//span').text
            except:
                name = "N/A"

            try:
                price = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
            except:
                price = "N/A"

            try:
                reviews = product.find_element(By.XPATH, './/span[@class="a-size-base s-underline-text"]').text
            except:
                reviews = "N/A"

            try:
                link_element = product.find_element(By.XPATH, './/a[contains(@href, "/dp/")]')
                product_url = link_element.get_attribute('href')
            except:
                product_url = "N/A"

            try:
                image_element = product.find_element(By.XPATH, './/img')
                image_url = image_element.get_attribute('src')
            except:
                image_url = "N/A"

            writer.writerow([name, price, reviews, product_url, image_url])

print(f"\n✅ Scraping completed! Data saved to '{csv_filename}'")
driver.quit()
