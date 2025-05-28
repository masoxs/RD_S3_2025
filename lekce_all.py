# All lectures:
# python - V
# ctrl + alt + l
y = 5 + 5
print(y)
x = 23
z = 4
y = x + 5 + z
print(type(x))
print(y)


# python -m venv --upgrade C:\Users\Precision\PycharmProjects\Project

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(15)

# Python 3: Fibonacci series for n th variable
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(15)


x = "ahoj"
len(x)
x.isupper()
"ahoj".upper()

"ahoj".upper().lower()
x = "ahoj".upper()
print(x)
##--------------------- Lekce 4 -----------------------------------------------------------------------------------

"""
What the Code is About
This code is a collection of examples demonstrating conditional statements (if, elif, else) and basic logic in Python. It shows how to:

Compare values (e.g., <, >, ==).
Use nested conditions.
Check membership in lists (in).
Handle user input and type conversion.
Work with Boolean logic (and, truthy/falsy values).
Use ternary operators for concise conditionals.
"""
x = 11
if x < 5:
    print("X je mensi nez 5")
elif x == 5:
    print("X je rovno 5")
elif x > 10:
    print("X je vetsi nez 10")
else:
    print("X je vetsi nez 5")

print("sbohem")

y = 1.5
if y < 5:
    print("y je mensi nez 5")
    if y < 2:
        print("y je take mensi nez 2")
        if y < 1:
            print("y je take mensi nez 1")
print("sbohem")

x = 8
if x < 6:
    print("x je mensi nez 6")
elif x == 8:
    print("x je 8")
else:
    print("stalo se neco jineho")

print("sbohem")

a = 3
b = 5
if a < 5 and b < 10:
    print("error")

x = [1,2,3,4]
if 4 in x:
    print("4 je v listu")

x = 7
z = "Ahoj" if x == 5 else "Sbohem"
if x == 5:
    y = "Ahoj"
else:
    y = "Sbohem"

print(y)
print(z)

is_good = True
if is_good:
    print("asdasd")

names = []

if names:
    print("retezec je naplnen")

name = ""
if name:
    print("jmeno je naplneno")

c = None
if c is None:
    print("C is none")

x = input("Zadej cislo: ")
x = int(x)

if x % 2 == 0:
    print("cislo je sude")
else:
    print("cislo je liche")

#--------------------- Lekce 5 ------------------------------------------------------------------------------------
import time
# For loop
start = time.time()
for i in range(10_000_000):
    pass
end = time.time()
print("For loop:", end - start)

# While loop
start = time.time()
i = 0
while i < 10_000_000:
    i += 1
end = time.time()
print("While loop:", end - start)

"""
výsledek:
For loop: 0.22839117050170898
While loop: 0.43266987800598145
"""
x = 0
while x < 10:
    if x == 7:
        end_this = True
    x = x + 1
    print(x)

# print("start")
# for i in range(10, 100, 10):
#     print(i)
# print("konec")

#
# names = ["Jirka", "Lenka", "Pavel", "Alice"]
#
# for name in names:
#     print(name)
#
# x = 5
#
# while x < 10:
#     x = x + 1
#     print("X je stale mensi nez 10, je: " + str(x))
# print("")

# names = ["Jirka", "Lenka", "Pavel", "Alice"]
#
# for name in names:
#     if 'L' in name:
#         break
#     print(name)

# x = 0
# end_this = False
# while x < 10:
#     if x == 7:
#         break
#     x = x + 1
#     print(x)


#
# numbers = [1,10,12,55,60]
#
# for n in numbers:
#     if n % 2 == 0:
#         continue
#     print(n)


# names = ["Jirka", "Lenka", "Pavel", "Alice"]
#
# for name in names:
#     for n in name:
#         if n == "a":
#             break
#         print(n)
#     print(name)

# chess_board = [["A1", "A2"], ["B1", "B2"], ["C1", "C2"]]
# new_chess_board = chess_board.copy()
#
# for board in chess_board:
#     new_chess_board.append("D")
#     for b in board:
#         print(b)


# numbers = [1,2,3] #10, 20, 30
#
# for n in numbers:
#     n = n*10
#     print(n)
#
# print(numbers)

# numbers = [1,2,3]
# # for i in range(len(numbers)):
# #     #print(numbers[i])
# #     numbers.append(numbers[i] * 10)
# #new_numbers = numbers.copy()
# new_numbers = []
# for n in numbers:
#     new_numbers.append(n*10)
# print(new_numbers)

# random_string_list = ["aaa", "b", "casxcjasjuidahjd", "jaduashd", "adad"]
# new_list = [s for s in random_string_list if len(s) > 3]
# print(new_list)

#is_running = True
# while True:
#     user_input = input("Tvoje instrukce? ")
#     if user_input == "konec":
#         print("Sbohem")
#         #is_running = False
#         break
#     print("Diky za instrukce")
#
# print("Konec programu")


# numbers = [1,2,3,4,5,2]
# for n in numbers:
#     print(n)
#     if n == 10:
#         print("Cyklus prerusen, 10")
#         break
# else:
#     print("10 nenalezeno")

numbers = [10,22,33,34,5,2]

for idx, value in enumerate(numbers):
    print(f"Index je: {idx}")
    print(f"Hodnota je: {value}")

#
# d = {"name":"Jirka", "age": 19, "class":"C"}
# for k, v in d.items():
#     print(k)
#     print(v)

# a_list = [1,2,3]
# b_list = ["a","b","c"]
#
# for a_val, b_val in zip(a_list, b_list):
#     print(a_val)
#     print(b_val)
#--------------------- Lekce 7 ------------------------------------------------------------------------------------

def power(n1: int, n2:int) -> int:
    return n1 ** n2

type(power(2,3))
def get_number() -> int:
    return 1

def get_numbers() -> tuple[int, int]:
    return 1, 2

type(get_numbers())
def print_name(name: str) -> None:
    print("Ahoj ", name)

print_name("Tomas")

x = get_number()

res = power(n1=4, n2=2)
print(res)

def work() -> None:
    x,y = get_numbers()
    print_name("Honza")
    print(get_number())

work()
res = get_numbers()
print(res)

def greet_user(name: str = "user") -> None:
    print("Hello, welcome to the system,", name)


greet_user()
greet_user("admin")

x = 1

def add_five(number: int) -> int:
    return number + 5

num = add_five(15)

def foo():
    print("calling")
    foo()

foo()

def print_reversed(num: int) -> None:
    if num == 0:
        return
    print(num)
    print_reversed(num - 1)
    print("ENDED FOR NUMBER", num)

print_reversed(3)

def test_generator():
    for i in range(5):
        yield i
        print("generator", i)
    print("generator end")

for x in test_generator():
    print(x)
def x_foo(a, b):
    return a + b

def sum(x, y):
    result = x + y

    return result

res = sum(10, 20)
print(res)

def add_numbers(a, b):
    if a == 0:
        return 0
    return a+b
#--------------------- Lekce 8 ------------------------------------------------------------------------------------


#--------------------- Lekce 9 ------------------------------------------------------------------------------------

#--------------------- Lekce 10 ------------------------------------------------------------------------------------

#--------------------- Lekce 11 ------------------------------------------------------------------------------------

#--------------------- Lekce 15 ------------------------------------------------------------------------------------

https://websockets.readthedocs.io/en/stable/
https://sqlitebrowser.org/dl/#windows




https://pytest-cov.readthedocs.io/en/latest/readme.html#
pytest --cov=bank_app --cov-report=term-missing tests/


https://martinfowler.com/

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
    city = "Houston"  # Example city for display

    # Fetch and process weather data
    weather = fetch_weather(lon, lat, units, appid, city)
    if weather:
        weather.display()
        save_to_database(weather)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()

class Foo:
    y = 6
    def __init__(self):
        self.x = 5
    @staticmethod
    def print_something():
        print("somthing")

    @classmethod
    def another_print(cls):
        print("somethig else")
        cls.print_something

