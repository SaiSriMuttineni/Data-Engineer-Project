## Solution 1: (Project) 
- Step 1: Scraping the worldbank website to fetch country names and the respective URL's that displays detailed statistics of each country.
- Step 2: Storing the data in sqlite3 database
- Step 3: Creating a API using Fast API using data from sqllite3, retrieving the data using API calls.
### Instructions for executing Solution 1:
- Install Python and Gitbash
- Import necessary libraries such as BeautifulSoup using the below command:
   - pip install requests beautifulsoup4 fastapi uvicorn
   - pip install fastapi uvicorn
- Open Gitbash and move to the Project folder in your desktop/laptop using cd command.
- Run the two code files namely Scraping.py and main.py using the below commands. If the files ran successfully, you should be able to see "world_bank_data.db"
    - python Scraping.py
    - python main.py
- If you want to verify/check/see the data stored in sqlite3, you can download sqlite3. Open bash and navigate to the sqlite3 folder. Use the below command to enter the database:
    - ./sqlite3.exe "path_to_db file/world_bank_data.db" 
    - The terminal is ready to use SQL queries and retrieve data.
- In the bash, run the below command to start the local server
    - uvicorn main:app --reload
    - The server is running at http://127.0.0.1:8000 and we can do API requests using /country/country_name to see the data related to that country. Ideally, we are displaying only Country Name and corresponding URL.
  
## Solution 2: (Project 1)
- Step 1: Scraping the worldbank website to fetch country names, the respective URL's and population data. (Vast number of API calls were made to get the population data)
- Step 2: Stored the data into .csv file.
### Instructions for executing Solution 2:
- All the necessary software is there to execute except the below command to support data extraction to .csv
    - pip install pandas
- Run the python code file Scrapper_Test.py using the below command. If the files ran succesfully, you should be able to see world_bank_data.csv file the same folder.
    - python Scrapper_Test.py
### Note: 
1. While running this code, since it is making API call to fetch population data for each country, we loss access to the website after some API calls and will not be able to retrieve the remaining data.
2. While we get the .csv file, we can make some visualizations in the Microsoft Excel to compare countries statistics.
3. I didn't create a API in this case.

## Conclusion:
- Overall, I enjoyed doing this challenging project while developing Solution 1. However, extracting just population data of each country is rough, because of having less idea on Frontend and becasue of multiple API calls and the website crash. But, I would like to continue the work to develop optimal solution. Thanks for the challenge.
