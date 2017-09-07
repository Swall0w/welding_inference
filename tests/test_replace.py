import unittest

import pandas as pd
from pandas.util.testing import assert_series_equal

from welding.replace import add_hour, iterative_hour_to_series


class AddHourTest(unittest.TestCase):
    def setUp(self):
        self.time = '00:15.5'

    def test_add_hour(self):
        self.assertEqual(add_hour(self.time), '00:00:15.5')


class IterativeHourSeriesTest(unittest.TestCase):
    def setUp(self):
        self.timeseries = pd.Series(['00:00:15.5',
                                     '00:31:26.0',
                                     '00:52:26.0',
                                     '00:10:26.0',
                                     '00:32:26.0',
                                     ])

        self.result = pd.Series(['00:00:15.5',
                                 '00:31:26.0',
                                 '00:52:26.0',
                                 '01:10:26.0',
                                 '01:32:26.0',
                                 ])

    def test_iterative_hour_seies(self):
        assert_series_equal(iterative_hour_to_series(self.timeseries),
                            self.result)


suite = unittest.TestLoader().loadTestsFromTestCase(IterativeHourSeriesTest)
unittest.TextTestRunner(verbosity=2).run(suite)
