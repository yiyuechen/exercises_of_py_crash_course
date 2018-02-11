from unittest import TestCase
from city_functions import get_city


class CityTestCase(TestCase):
    """test city_functions.py"""

    def test_city_country(self):
        """test if get_city could return a formatted string"""
        city_info = get_city('Shanghai', 'China')
        self.assertEqual(city_info, 'Shanghai, China')


