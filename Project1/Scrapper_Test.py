import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_world_bank_data():
    base_url = 'https://data.worldbank.org'
    url = f'{base_url}/country'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a list to store data
    country_data = []

    # Scraping country links (update based on actual website structure)
    for country_link in soup.find_all('a', href=True):
        if '/country/' in country_link['href']:
            country_name = country_link.text.strip()
            country_url = base_url + country_link['href']

            # Extract additional data from the country page
            # Modify the below data extraction based on the actual HTML structure of country-specific pages
            try:
                # Now scrape individual country page for additional data
                print(country_url)
                country_response = requests.get(country_url)
                country_soup = BeautifulSoup(country_response.text, 'html.parser')
                # Find the parent div with id '0'
                parent_div = country_soup.find('div', {'class': 'indicator-item', 'id': '0'})

                # Find all children with class "indicator-item__wrapper"
                wrapper_divs = parent_div.find_all('div', class_='indicator-item__wrapper')

                # Access the third child (index 2 since it is zero-based indexing)
                third_child = wrapper_divs[2]

                # Find the div containing the population value within the third child
                population_div = third_child.find('div', class_='indicator-item__data-info')

                # Extract the population value (text inside the span)
                population_value = population_div.find('span').text

                # Append the extracted data into the list
                country_data.append({
                    "Country": country_name,
                    "URL": country_url,
                    "Population": population_value
                })
            except AttributeError:
                print(f"Could not find data for {country_name}")

    # Convert list of dictionaries to pandas DataFrame
    df = pd.DataFrame(country_data)
    
    # Save to CSV for further analysis and visualization
    df.to_csv('world_bank_data.csv', index=False)

    return df

# Call the function to scrape and save data
scraped_data = scrape_world_bank_data()
