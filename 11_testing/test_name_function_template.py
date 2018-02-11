# This file is not used.

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test name_function"""

    def test_first_last_name(self):
        """test if formatting works"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
