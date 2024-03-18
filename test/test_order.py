import pytest

from src.address import Address
from src.product import (
    Product,
    red_guitar,
    blue_guitar,
    green_guitar,
    yellow_guitar,
    purple_guitar,
    black_guitar,
)
from src.countries import Country
from src.order import Order


def test_create_order():
    address = Address(
        house="House 1",
        street="Street",
        city="City",
        postcode="X12 3YZ",
        country=Country.UNITED_KINGDOM,
    )

    items = [black_guitar]

    order = Order(
        shipping_address=address,
        items=items,
    )

    assert order.shipping_address == address
    assert order.items == [black_guitar]
