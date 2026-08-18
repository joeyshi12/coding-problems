"""
Problem 1.1: Inventory and Reorder System

Design and implement a small object oriented system for a supply
inventory manager.

Base requirements:
    - Track items with a name, quantity on hand, and unit price.
    - Support adding stock, removing stock, and querying current quantity.
    - Handle an error when removing more stock than is available.
    - Generate a low stock report: items below a configurable reorder
      threshold.

Follow up extensions (attempt only after your base version works):
    1. Add suppliers. Each item can have multiple suppliers with
       different prices and lead times. Add a method that recommends
       the cheapest supplier for a reorder.
    2. Add categories. Perishable items also track an expiration date
       and can be queried for items expiring within N days.
    3. Add a transaction log. Every stock change is recorded with a
       timestamp and reason. Reconstruct quantity on hand at any past
       point from the log.

Focus on: class boundaries, encapsulation, extensibility, and edge
cases (zero or negative quantities, missing items, duplicate suppliers).
"""

from dataclasses import dataclass


class OutOfStockError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


@dataclass
class Item:
    name: str
    quantity: int
    unit_price: float
    reorder_threshold: int = 0


class Inventory:
    def __init__(self):
        # TODO: choose a data structure to hold items
        pass

    def add_item(self, name: str, quantity: int, unit_price: float,
                 reorder_threshold: int = 0) -> None:
        """Add a new item, or increase quantity if it already exists."""
        raise NotImplementedError

    def remove_stock(self, name: str, quantity: int) -> None:
        """Remove stock. Raise OutOfStockError if quantity is insufficient."""
        raise NotImplementedError

    def get_quantity(self, name: str) -> int:
        raise NotImplementedError

    def low_stock_report(self) -> list:
        """Return items at or below their reorder threshold."""
        raise NotImplementedError


# ---------------------------------------------------------------------
# Extension 1: Suppliers
# ---------------------------------------------------------------------

@dataclass
class Supplier:
    name: str
    price: float
    lead_time_days: int


class InventoryWithSuppliers(Inventory):
    def add_supplier(self, item_name: str, supplier: Supplier) -> None:
        raise NotImplementedError

    def cheapest_supplier(self, item_name: str) -> Supplier:
        raise NotImplementedError


# ---------------------------------------------------------------------
# Extension 2: Categories / perishables
# ---------------------------------------------------------------------

# TODO: extend Item or add a PerishableItem subclass with an
# expiration_date field, plus a method to query items expiring
# within N days.


# ---------------------------------------------------------------------
# Extension 3: Transaction log
# ---------------------------------------------------------------------

# TODO: add a log of (timestamp, item_name, delta, reason) entries and
# a method to reconstruct quantity on hand at a given past timestamp.


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("flour", quantity=10, unit_price=2.5, reorder_threshold=5)
    inv.remove_stock("flour", 3)
    assert inv.get_quantity("flour") == 7

    try:
        inv.remove_stock("flour", 100)
        assert False, "expected OutOfStockError"
    except OutOfStockError:
        pass

    inv.remove_stock("flour", 3)
    report = inv.low_stock_report()
    assert any(item.name == "flour" for item in report)

    print("All basic checks passed.")
