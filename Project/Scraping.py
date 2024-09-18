import requests
from bs4 import BeautifulSoup
import sqlite3
import re

# Scrape World Bank country data
def scrape_world_bank_data():
    url = "https://data.worldbank.org/country"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(response.text)
    countries_data = []
    country_list = soup.find_all('a', href=re.compile(r'^/country/.*\?view=chart'))
    
    for country in country_list:
        country_name = country.get_text()
        country_url = 'https://data.worldbank.org'+country['href']
        countries_data.append((country_name, country_url))
    
    # Print the scraped data for verification
    #print(f"Scraped data: {countries_data}")
    
    return countries_data

# Save the scraped data into a SQLite database
def save_data_to_db(data):
    conn = sqlite3.connect('C:/Users/sm4332/OneDrive - Northern Arizona University/Downloads/OneDrive - Northern Arizona University/Desktop/Project/world_bank_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT
        )
    ''')
    
    cursor.executemany('''
        INSERT INTO countries (name, url) VALUES (?, ?)
    ''', data)
    
    conn.commit()
    conn.close()

# Running the scraping and storing process
data = scrape_world_bank_data()
print(data)
save_data_to_db(data)
