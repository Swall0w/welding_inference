import unittest

from welding.convert import (parse_time,
                             convert_time_to_index,
                             _datetime_to_second)


class ParseTimeTest(unittest.TestCase):
    def setUp(self):
        self.time = parse_time('00:15.5')

    def test_parse_test(self):
        self.assertEqual(self.time.minute, 0)
        self.assertEqual(self.time.second, 15)
        self.assertEqual(self.time.microsecond, 500000)


class DatetimeToSecondTest(unittest.TestCase):
    def setUp(self):
        self.time = parse_time('00:15.5')

    def test_datetime_to_second(self):
        self.assertEqual(_datetime_to_second(self.time), 15.5)


class ConvertTimeIndexTest(unittest.TestCase):
    def setUp(self):
        self.timecode = parse_time('00:15.5')
        self.fps = 10

    def test_convert_time_to_index(self):
        self.assertEqual(convert_time_to_index(self.timecode, self.fps),
                         float(155))
