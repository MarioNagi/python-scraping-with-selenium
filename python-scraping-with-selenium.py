import pandas as pd
import smtplib
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

Amazon_link="https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_Items(driver):
    items_DIV_TAG = 'DealGridItem-module__dealItem_2X_WLYkJ3-dM0LtXI9THcu'
    driver.get(Amazon_link)

    items = driver.find_elements(By.CLASS_NAME, items_DIV_TAG)
    return items

def parse_item(item):
    
    item_name_tag = item.find_element(By.CLASS_NAME, 'DealContent-module__truncate_sWbxETx42ZPStTc9jwySW')
    item_name = item_name_tag.text
    url_tag=item.find_element(By.CLASS_NAME, 'a-link-normal')
    url = url_tag.get_attribute('href')

    thumbnail_tag = item.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    try:
        price_div = item.find_element(By.CLASS_NAME, 'a-price-whole')
        price = price_div.text
    except NoSuchElementException:
        print("NoSuchElementException")
        price="No Price Found"


    #description = item.find_element(By.ID, 'description-text').text

    return {
    'item_name': item_name,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'price': price,
    #'description': description
  }


if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()

    print('Fetching Top items')
    items = get_Items(driver)
  
    print('Parsing top 10 videos')
    items_data = [parse_item (item) for item in items]
#    print( items_data)
    print('Save the data to a CSV')
    items_df = pd.DataFrame(items_data)
    print(items_df)
    items_df.to_csv('top10items.csv', index=None)
