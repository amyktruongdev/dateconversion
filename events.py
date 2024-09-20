import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# Set up ChromeDriver using webdriver-manager to handle the driver installation
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 1: Open the webpage
driver.get('https://news.csun.edu/events/category/usu/list/')

# Step 2: Get page source after JavaScript has loaded
page_source = driver.page_source

# Step 3: Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Step 4: Find all span tags with class 'tribe-event-date-start'
span_tags = soup.find_all('span', class_='tribe-event-date-start')
end_time = soup.find_all('span', class_='tribe-event-time')

# Step 5: Print the content of each found span tag
for span, meow in zip(span_tags, end_time):
    print(span.text + " to " + meow.text)

# Step 6: Close the browser
driver.quit()
