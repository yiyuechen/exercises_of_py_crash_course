from unittest import TestCase
from city_functions import get_city


class CityTestCase(TestCase):
    """test city_functions.py"""

    def test_city_country(self):
        """test if get_city could return a formatted string"""
        city_info = get_city('Shanghai', 'China', population=5000000)
        self.assertEqual(city_info, 'Shanghai, China - population 5000000')
