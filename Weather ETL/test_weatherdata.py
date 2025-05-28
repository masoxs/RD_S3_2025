import unittest
import io
import sys
from datetime import datetime

class TestWeatherData(unittest.TestCase):
    def setUp(self):
        # Initialize a WeatherData object with sample data for all tests
        self.weather = WeatherData(
            date="2025-05-28",
            temperature=25.5,
            condition="clear sky",
            city="Houston",
            lon=-94.04,
            lat=33.44,
            units="metric"
        )

    def test_display(self):
        # Capture the output of display method
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout
        self.weather.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        expected_output = "Weather in Houston on 2025-05-28: clear sky, 25.5°C\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_empty_condition(self):
        # Test display with empty condition
        weather = WeatherData(
            date="2025-05-28",
            temperature=0,
            condition="",
            city="Houston",
            lon=-94.04,
            lat=33.44,
            units="metric"
        )
        captured_output = io.StringIO()
        sys.stdout = captured_output
        weather.display()
        sys.stdout = sys.__stdout__
        expected_output = "Weather in Houston on 2025-05-28: , 0°C\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_to_dict(self):
        # Test to_dict returns correct dictionary
        expected_dict = {
            "date": "2025-05-28",
            "temperature": 25.5,
            "condition": "clear sky",
            "city": "Houston",
            "lon": -94.04,
            "lat": 33.44,
            "units": "metric"
        }
        self.assertEqual(self.weather.to_dict(), expected_dict)

    def test_to_dict_with_none_values(self):
        # Test to_dict with None condition
        weather = WeatherData(
            date="2025-05-28",
            temperature=0,
            condition=None,
            city="Houston",
            lon=-94.04,
            lat=33.44,
            units=None
        )
        expected_dict = {
            "date": "2025-05-28",
            "temperature": 0,
            "condition": None,
            "city": "Houston",
            "lon": -94.04,
            "lat": 33.44,
            "units": None
        }
        self.assertEqual(weather.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()