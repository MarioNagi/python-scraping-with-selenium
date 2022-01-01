# Python-scraping-with-selenium

This Tutorial is using python and selenium to scrap dynamic websites like Amazon store website, as Soup library can only scrap static websites


## About Selenium:
selenium is a headless -non-GUI- browser able to load dynamic websites like a normal browser and returns the whole page html code

## Install Selenium:
first step is to install selenium via pip 

pip install selenium

after that you have to download the driver, choose any driver like Google, Firefox, etc

https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

please note that, the web driver version must be the same as your website driver


## Registering the driver and getting the data:

after Registering the driver, you can retrieve the web page code and start parsing the data to get the items details (Name, thumbnail, URL, price)
adding all of the above attributes in a list then exporting it to pandas and saved to CSV file
