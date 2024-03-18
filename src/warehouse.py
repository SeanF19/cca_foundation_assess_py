from dataclasses import dataclass
from .product import Product
from .order import Item


@dataclass
class Entry:
    product: Product
    stock: int

    @property
    def product_id(self):
        return self.product.id


class Warehouse:
    def __init__(self, catalogue: list[Entry]):
        self.catalogue: dict[int, Entry] = {}

        for entry in catalogue:
            self.add_stock(entry)

    def add_stock(self, entry: Entry) -> None:
        if not (catalogue_entry := self.catalogue.get(entry.product_id)):
            self.catalogue[entry.product_id] = entry
        else:
            catalogue_entry.stock += entry.stock
            self.catalogue[entry.product_id] = catalogue_entry

    def check_stock_available(self, item: Item) -> bool:
        return item.quantity <= self.catalogue[item.product.id].stock

    def remove_stock(self, item: Item) -> None:
        if self.check_stock_available(item):
            entry = self.catalogue[item.product.id]
            entry.stock -= item.quantity
            self.catalogue[item.product.id] = entry
        else:
            raise Exception(f"Not enough stock: {item.product}")
