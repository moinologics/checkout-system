import unittest
from unittest.mock import patch
from checkout import SupermarketCheckout

class TestSupermarketCheckout(unittest.TestCase):
  def setUp(self):
    pricing = {
    	'A': {'unit': 50, 'special': (3, 130)},  # 3 for 130
    	'B': {'unit': 30, 'special': (2, 45)},   # 2 for 45
    	'C': {'unit': 20},                       # no special price
    	'D': {'unit': 15}                        # no special price
  	}
    self.checkout = SupermarketCheckout(pricing)

  def test_empty_cart(self):
    # no items
    self.assertEqual(self.checkout.calculate_total(""), 0)

  def test_single_item_prices(self):
    # individual items
    self.assertEqual(self.checkout.calculate_total("A"), 50)
    self.assertEqual(self.checkout.calculate_total("B"), 30)
    self.assertEqual(self.checkout.calculate_total("C"), 20)
    self.assertEqual(self.checkout.calculate_total("D"), 15)

  def test_multiple_items(self):
    # multiple items without special pricing
    self.assertEqual(self.checkout.calculate_total("AB"), 80)
    self.assertEqual(self.checkout.calculate_total("CDBA"), 115)

  def test_special_deals(self):
    # items with special pricing
    self.assertEqual(self.checkout.calculate_total("AAA"), 130)
    self.assertEqual(self.checkout.calculate_total("BB"), 45)
    self.assertEqual(self.checkout.calculate_total("AAAA"), 180)
    self.assertEqual(self.checkout.calculate_total("BBBB"), 90)

  def test_mixed_items(self):
    # mix of regular and special prices
    self.assertEqual(self.checkout.calculate_total("AAAB"), 160)
    self.assertEqual(self.checkout.calculate_total("AAABB"), 175)
    self.assertEqual(self.checkout.calculate_total("AAABBD"), 190)
    self.assertEqual(self.checkout.calculate_total("DABABA"), 190)

  @patch('builtins.print')
  def test_invalid_items(self, mock_print):
    # items not in the price list
    self.assertEqual(self.checkout.calculate_total("E"), 0)       # Ignore unknown item
    mock_print.assert_called_with("Item 'E' not in the pricing list, skipping...")
    self.assertEqual(self.checkout.calculate_total("AAAE"), 130)  # Ignore E, process A
    mock_print.assert_called_with("Item 'E' not in the pricing list, skipping...")

if __name__ == "__main__":
	test = unittest.TestLoader().loadTestsFromTestCase(TestSupermarketCheckout)
	unittest.TextTestRunner(verbosity=2).run(test)
