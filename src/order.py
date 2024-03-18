from dataclasses import dataclass

from .address import Address
from .product import Product


@dataclass
class Item:
    product: Product
    quantity: int

    @property
    def item_price(self) -> float:
        return float(self.product.price * self.quantity)


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def calculate_shipping(self):
        pass
