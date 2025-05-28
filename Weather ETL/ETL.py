import requests
import sqlite3
from datetime import datetime

# WeatherData class to store and display data
class WeatherData:
    def __init__(self, date, temperature, condition, city, lon, lat, units):
        self.date = date
        self.temperature = temperature
        self.condition = condition
        self.city = city
        self.lon = lon
        self.lat = lat
        self.units = units

    def display(self):
        print(f"Weather in {self.city} on {self.date}: {self.condition}, {self.temperature}°C")

    def to_dict(self):
        return {
            "date": self.date,
            "temperature": self.temperature,
            "condition": self.condition,
            "city": self.city,
            "lon": self.lon,
            "lat": self.lat,
            "units": self.units
        }

# Fetch weather data from the API
def fetch_weather(lon, lat, units, appid, city):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&appid={appid}"
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors (e.g., 401, 404)
        data = response.json()  # Parse JSON response

        # Extract and transform data
        date = datetime.now().strftime("%Y-%m-%d")
        temperature = data["current"]["temp"]  # One Call API uses 'current'
        condition = data["current"]["weather"][0]["description"]

        return WeatherData(date, temperature, condition, city, lon, lat, units)

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or API server is down.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: API request failed with status code {e.response.status_code}.")
        return None
    except requests.exceptions.JSONDecodeError:
        print("Error: Failed to parse API response.")
        return None
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during data fetch: {e}")
        return None

# Save weather data to SQLite database
def save_to_database(weather_data):
    if weather_data is None:
        print("No data to save.")
        return

    try:
        # Connect to the database
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()

        # Create table if it doesn’t exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                date TEXT,
                temperature REAL,
                condition TEXT,
                city TEXT,
                lon REAL,
                lat REAL,
                units TEXT
            )
        """)

        # Insert data
        cursor.execute("""
            INSERT INTO weather (date, temperature, condition, city, lon, lat, units)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (weather_data.date, weather_data.temperature, weather_data.condition,
              weather_data.city, weather_data.lon, weather_data.lat, weather_data.units))

        conn.commit()

    except sqlite3.OperationalError as e:
        print(f"Database connection error: {e}")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting data into database: {e}")
    except Exception as e:
        print(f"Unexpected database error: {e}")
    finally:
        # Always close the connection
        if 'conn' in locals():
            conn.close()

# Main function to run the ETL process
def main():
    lat = 33.44
    lon = -94.04
    units = "metric"  # For Celsius
    appid = "811543ad77158843bef8efe9f246a8c140"  # Replace with your actual OpenWeatherMap API key
    city = "Texas"  # Example city for display

    # Fetch and process weather data
    weather = fetch_weather(lon, lat, units, appid, city)
    if weather:
        weather.display()
        save_to_database(weather)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()