"""
Upravte svůj projekt tak, aby alespoň jedna klíčová část (například položka, uživatel nebo jiná důležitá věc ve vašem projektu) byla reprezentována jako třída.
Tato třída bude obsahovat:
Vlastnosti (atributy): informace, které popisují tuto věc.
Metody: akce, které s touto věcí můžeme provádět
"""

class WeatherData:
    def __init__(self, date, temperature, condition, city): #sets up a new WeatherData object with the provided data.
        self.date = date
        self.temperature = temperature
        self.condition = condition
        self.city = city

    def display(self): #provides a human-readable output of the weather data.
        print(f"Weather in {self.city} on {self.date}: {self.condition}, {self.temperature}°C")

    def to_dict(self): #converts the object’s data into a dic or DF
        return {
            "date": self.date,
            "temperature": self.temperature,
            "condition": self.condition,
            "city": self.city
        }