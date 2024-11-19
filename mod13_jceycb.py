import unittest
from datetime import datetime

# Validation functions for inputs
def validate_symbol(symbol):
    """Validate that the symbol is 1-7 uppercase alphabetic characters."""
    return symbol.isalpha() and 1 <= len(symbol) <= 7 and symbol.isupper()

def validate_chart_type(chart_type):
    """Validate that chart type is a numeric value of 1 or 2."""
    return chart_type.isdigit() and int(chart_type) in [1, 2]

def validate_time_series(time_series):
    """Validate that time series is a numeric value between 1 and 4."""
    return time_series.isdigit() and int(time_series) in range(1, 5)

def validate_date(date_str):
    """Validate that the date is in YYYY-MM-DD format and is a valid date."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Unit test class
class TestInputs(unittest.TestCase):

    # Test for symbol validation
    def test_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))  # Valid symbol
        self.assertTrue(validate_symbol("GOOGL"))  # Valid symbol
        self.assertFalse(validate_symbol("apple"))  # Not uppercase
        self.assertFalse(validate_symbol("123"))    # Contains digits
        self.assertFalse(validate_symbol("TOOLONGSYMBOL"))  # Too long

    # Test for chart type validation
    def test_chart_type(self):
        self.assertTrue(validate_chart_type("1"))  # Valid chart type
        self.assertTrue(validate_chart_type("2"))  # Valid chart type
        self.assertFalse(validate_chart_type("0"))  # Out of range
        self.assertFalse(validate_chart_type("3"))  # Out of range
        self.assertFalse(validate_chart_type("a"))  # Not numeric

    # Test for time series validation
    def test_time_series(self):
        self.assertTrue(validate_time_series("1"))  # Valid time series
        self.assertTrue(validate_time_series("4"))  # Valid time series
        self.assertFalse(validate_time_series("0"))  # Out of range
        self.assertFalse(validate_time_series("5"))  # Out of range
        self.assertFalse(validate_time_series("x"))  # Not numeric

    # Test for start date validation
    def test_start_date(self):
        self.assertTrue(validate_date("2023-11-19"))  # Valid date
        self.assertFalse(validate_date("19-11-2023"))  # Incorrect format
        self.assertFalse(validate_date("2023/11/19"))  # Incorrect format
        self.assertFalse(validate_date("2023-13-19"))  # Invalid month

    # Test for end date validation
    def test_end_date(self):
        self.assertTrue(validate_date("2023-12-31"))  # Valid date
        self.assertFalse(validate_date("2023-02-30"))  # Invalid day
        self.assertFalse(validate_date("not-a-date"))  # Not a date format

# Run tests when the script is executed
if __name__ == "__main__":
    unittest.main()
