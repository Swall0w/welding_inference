import unittest

from welding.replace import add_hour


class AddHourTest(unittest.TestCase):
    def setUp(self):
        self.time = '00:15.5'

    def test_add_hour(self):
        self.assertEqual(add_hour(self.time), '00:00:15.5')
