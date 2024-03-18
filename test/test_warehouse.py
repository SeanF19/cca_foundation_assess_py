import pytest

from src.warehouse import Warehouse, Entry
from src.product import (
    Product,
    red_guitar,
    blue_guitar,
    green_guitar,
    yellow_guitar,
    purple_guitar,
    black_guitar,
)


def test_create_warehouse():
    catalogue = [
        Entry(product=red_guitar, stock=5),
        Entry(product=blue_guitar, stock=4),
        Entry(product=green_guitar, stock=12),
    ]
    warehouse = Warehouse(catalogue)

    assert warehouse.catalogue[red_guitar.id].stock == 5
    assert warehouse.catalogue[blue_guitar.id].stock == 4
    assert warehouse.catalogue[green_guitar.id].stock == 12
