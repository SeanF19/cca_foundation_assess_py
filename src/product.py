from dataclasses import dataclass


@dataclass
class Product:
    id: int
    description: str
    price: float


red_guitar = Product(
    id=1,
    description="Red Guitar",
    price=100,
)

blue_guitar = Product(
    id=2,
    description="Blue Guitar",
    price=70,
)

green_guitar = Product(
    id=3,
    description="Green Guitar",
    price=85,
)

yellow_guitar = Product(
    id=4,
    description="Yellow Guitar",
    price=110,
)

purple_guitar = Product(
    id=5,
    description="Purple Guitar",
    price=120,
)

black_guitar = Product(
    id=6,
    description="Black Guitar",
    price=60,
)
