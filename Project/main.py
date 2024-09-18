from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Function to get the data of a country from SQLite
def get_country_data(country_name):
    conn = sqlite3.connect('C:/Users/sm4332/OneDrive - Northern Arizona University/Downloads/OneDrive - Northern Arizona University/Desktop/Project/world_bank_data.db')
    print("Entered")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, url FROM countries WHERE name LIKE ?", (f'%{country_name}%',))
    country = cursor.fetchone()
    
    conn.close()

    print(f"Query executed for {country_name}")
    print(f"Result from DB: {country}")
    
    return country

@app.get("/country/{country_name}")
def read_country(country_name: str):
    country = get_country_data(country_name)
    if country:
        return {"name": country[0], "url": country[1]}
    else:
        raise HTTPException(status_code=404, detail="Country not found")

@app.get("/")
def root():
    return {"message": "Welcome to the World Bank Country API. Use /country/{India} to get country details."}
