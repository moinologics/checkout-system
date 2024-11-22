from typing import Dict, Optional, Tuple, TypedDict

class ItemPricing(TypedDict):
  unit: int
  special: Optional[Tuple[int, int]]

PricingDict = Dict[str, ItemPricing]

class SupermarketCheckout:
  prices: PricingDict

  def __init__(self, prices: PricingDict):
    self.prices = prices

  def calculate_total(self, cart):
    # count frequancy of each item
    counts = {}
    for item in cart:
      counts[item] = counts.get(item, 0) + 1

    total = 0

    for item, count in counts.items():
      if item not in self.prices:
        print(f"Item '{item}' not in the pricing list, skipping...")
        continue

      price_info = self.prices[item]
      unit_price = price_info['unit']
      special = price_info.get('special')

      if special:
        quantity, price = special
        offer_items_count = count // quantity
        normal_items_count = count % quantity
        total_price_of_item = offer_items_count * price + normal_items_count * unit_price
        total += total_price_of_item
      else:
        total += count * unit_price

    return total

if __name__ == "__main__":

  pricing = {
    'A': {'unit': 50, 'special': (3, 130)},  # 3 for 130
    'B': {'unit': 30, 'special': (2, 45)},   # 2 for 45
    'C': {'unit': 20},                       # no special price
    'D': {'unit': 15}                        # no special price
  }

  checkout = SupermarketCheckout(pricing)

  print("press ctrl+c for exit\n")

  while True:
    try:
      cart_items = input("Enter cart Items String: ")
      cart_total = checkout.calculate_total(cart_items)
      print("total Price for the cart: ", cart_total)
    except KeyboardInterrupt:
      print("\n\nprogram ended by the user")
      break
