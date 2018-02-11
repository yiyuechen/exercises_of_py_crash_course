from unittest import TestCase
from name_function import get_formatted_name


class TestGet_formatted_name(TestCase):
    pass

    def test_first_last_name(self):
        """test if formatting works"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
