"""
Problem 1.2: Recipe and Shopping List Generator

Design a system that:
    - Stores recipes made of ingredients with quantities and units.
    - Given a set of recipes and a known pantry inventory, generates a
      shopping list of missing items.
    - Handles unit conversions where reasonable (tsp to tbsp to cup).
      Decide how far to take this and be ready to explain the scope
      decision.

Extension:
    Support scaling a recipe up or down (serve 6 instead of 4) and
    update the shopping list accordingly.
"""

from dataclasses import dataclass, field


@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str


@dataclass
class Recipe:
    name: str
    servings: int
    ingredients: list  # list[Ingredient]

    def scaled(self, target_servings: int) -> "Recipe":
        """Return a new Recipe scaled to target_servings."""
        raise NotImplementedError


class Pantry:
    """Tracks what the user already has on hand."""

    def __init__(self):
        # TODO: choose a data structure, e.g. dict[(name, unit)] -> quantity
        pass

    def add(self, name: str, quantity: float, unit: str) -> None:
        raise NotImplementedError

    def has_quantity(self, name: str, quantity: float, unit: str) -> bool:
        raise NotImplementedError


# Minimal unit conversion table -- extend as needed, or decide to keep
# scope small and explain that decision out loud.
UNIT_CONVERSIONS = {
    ("tsp", "tbsp"): 1 / 3,
    ("tbsp", "tsp"): 3,
    ("tbsp", "cup"): 1 / 16,
    ("cup", "tbsp"): 16,
}


def convert(quantity: float, from_unit: str, to_unit: str) -> float:
    """Convert quantity from from_unit to to_unit. Raise ValueError if
    the conversion isn't supported."""
    raise NotImplementedError


def generate_shopping_list(recipes: list, pantry: Pantry) -> list:
    """
    Given a list of Recipe objects and a Pantry, return a list of
    Ingredient objects representing what still needs to be bought.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    pancakes = Recipe(
        name="Pancakes",
        servings=4,
        ingredients=[
            Ingredient("flour", 2, "cup"),
            Ingredient("sugar", 2, "tbsp"),
            Ingredient("milk", 1.5, "cup"),
        ],
    )

    pantry = Pantry()
    pantry.add("flour", 1, "cup")
    pantry.add("sugar", 6, "tbsp")

    shopping_list = generate_shopping_list([pancakes], pantry)
    missing_names = {i.name for i in shopping_list}
    assert "flour" in missing_names
    assert "milk" in missing_names
    assert "sugar" not in missing_names

    scaled = pancakes.scaled(8)
    assert scaled.servings == 8

    print("All basic checks passed.")
