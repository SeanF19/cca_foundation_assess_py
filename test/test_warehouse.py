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
from src.order import Item


@pytest.mark.parametrize(
    "entries, expected_stock",
    [
        (
                [
                    Entry(product=red_guitar, stock=5),
                    Entry(product=blue_guitar, stock=4),
                    Entry(product=green_guitar, stock=12),
                ],
                {
                    red_guitar.id: 5,
                    blue_guitar.id: 4,
                    green_guitar.id: 12,
                }
        ),
        (
                [
                    Entry(product=red_guitar, stock=5),
                    Entry(product=blue_guitar, stock=4),
                    Entry(product=green_guitar, stock=12),
                    Entry(product=green_guitar, stock=3),
                    Entry(product=red_guitar, stock=4),
                ],
                {
                    red_guitar.id: 9,
                    blue_guitar.id: 4,
                    green_guitar.id: 15,
                }
        ),
    ]
)
def test_create_warehouse(entries: list[Entry], expected_stock: dict[int, int]):
    warehouse = Warehouse(entries)

    for product_id, stock in expected_stock.items():
        assert warehouse.catalogue[product_id].stock == stock


@pytest.mark.parametrize(
    "item, expected_response, expected_stock",
    [
        (Item(product=red_guitar, quantity=3), True, 2),
        (Item(product=red_guitar, quantity=5), True, 0),
        (Item(product=red_guitar, quantity=6), False, 5),
    ]
)
def test_check_stock(item: Item, expected_response: bool, expected_stock: int):
    warehouse = Warehouse(
        [
            Entry(product=red_guitar, stock=5),
            Entry(product=blue_guitar, stock=4),
            Entry(product=green_guitar, stock=12),
        ]
    )
    assert warehouse.check_stock(item) is expected_response
    assert warehouse.catalogue[item.product.id].stock == expected_stock
