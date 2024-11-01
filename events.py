from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

#ChromeDriver using webdriver-manager to handle the driver installation
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://news.csun.edu/events/category/usu/page/2/')

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

span_tags = soup.find_all('span', class_='tribe-event-date-start')
end_time_tags = soup.find_all('span', class_='tribe-event-time')

data = []

for start, end in zip(span_tags, end_time_tags):
    item = {}
    item['Start Date'] = start.text.strip() 
    item['End Time'] = end.text.strip()       
    data.append(item)


df = pd.DataFrame(data)
output_file = 'events_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
driver.quit()
