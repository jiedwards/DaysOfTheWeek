import unittest
from daysOfTheWeek import dayReturn

class daysOfTheWeekTests(unittest.TestCase):

	def test_day_return_invalid_day(self):
		self.assertTrue(dayReturn("Wednesday", 90) == "Invalid day entered")

	def test_day_return_invalid_dayIncrement(self):
		self.assertTrue(dayReturn("Mon", -1) == "Invalid entry")

	def test_day_return_valid_same_week_result(self):
		self.assertTrue(dayReturn("Mon", 2) == "Wed")

	def test_day_return_valid_different_week_result(self):
		self.assertTrue(dayReturn("Mon", 37) == "Wed")


if __name__=='__main__':
	unittest.main()