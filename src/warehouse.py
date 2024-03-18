from dataclasses import dataclass
from .product import Product


@dataclass
class Entry:
    product: Product
    stock: int

    @property
    def product_id(self):
        return self.product.id


class Warehouse:
    catalogue: dict[int, Entry] = {}

    def __init__(self, catalogue: list[Entry]):
        for entry in catalogue:
            self.add_stock(entry)

    def add_stock(self, entry: Entry) -> None:
        if not (catalogue_entry := self.catalogue.get(entry.product_id)):
            self.catalogue[entry.product_id] = entry
        else:
            catalogue_entry.stock += entry.stock
            self.catalogue[entry.product_id] = catalogue_entry
