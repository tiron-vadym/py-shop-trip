from typing import List
from app.shop import Shop
from app.car import Car
from app import parsing

from decimal import Decimal
import math


class Customer:
    def __init__(
            self,
            name: str,
            location: List[int],
            money: float,
            product_cart: dict,
            car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def calculate_fuel_cost(self, car: Car, shop: Shop) -> Decimal:
        fuel_price = parsing.parse_data_from_json()["FUEL_PRICE"]
        distance = math.sqrt((shop.location[0] - self.location[0]) ** 2
                             + (shop.location[1] - self.location[1]) ** 2)
        fuel_cost = (fuel_price * car.fuel_consumption / 100) * distance
        return Decimal(fuel_cost)

    def calculate_product_cost(self, shop: Shop) -> Decimal:
        product_cost = Decimal("0")
        for key in self.product_cart:
            if key in shop.products:
                product_cost += (Decimal(self.product_cart[key])
                                 * Decimal(shop.products[key]))
        return product_cost
