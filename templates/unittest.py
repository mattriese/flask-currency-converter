from logic import convert
from unittest import TestCase

class ConvertTestCase(TestCase):
	"""unittest of convert(), testing converting 1 USD to USD"""

	def test_convert(self):
		self.assertEqual(convert('USD', 'USD', 1), 1)
