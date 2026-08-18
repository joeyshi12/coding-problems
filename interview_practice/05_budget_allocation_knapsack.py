"""
Problem 2.3: Dynamic Programming -- Budget Allocation

Given a daily ad budget and a list of campaigns with cost and expected
return, choose a subset that maximizes return without exceeding
budget (0/1 knapsack).

Extension: campaigns can be partially funded for a prorated return
(fractional knapsack).
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Campaign:
    name: str
    cost: float
    expected_return: float


def max_return_0_1(budget: float, campaigns: List[Campaign]) -> float:
    """
    Return the maximum total expected return achievable by fully
    funding a subset of campaigns without exceeding budget.
    """
    raise NotImplementedError


def max_return_fractional(budget: float, campaigns: List[Campaign]) -> float:
    """
    Return the maximum total expected return achievable when
    campaigns can be partially funded, with prorated return.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    campaigns = [
        Campaign("search", cost=60, expected_return=100),
        Campaign("display", cost=50, expected_return=60),
        Campaign("video", cost=20, expected_return=60),
    ]

    # 0/1 knapsack with budget 50: best is "video" alone (60) vs
    # "display" alone (60) -- either is valid, check the value.
    assert max_return_0_1(50, campaigns) == 60

    assert max_return_0_1(70, campaigns) == 120  # display + video

    # Fractional: with budget 50, take all of "video" (20 cost, 60
    # return) then 30/60 of "display" (30 cost, 36 return) = 96
    result = max_return_fractional(50, campaigns)
    assert abs(result - 96) < 1e-6

    print("All basic checks passed.")
