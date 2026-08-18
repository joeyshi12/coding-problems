"""
Problem 2.4: Sliding Window -- Click Fraud Detector

Given a stream of timestamped ad clicks by user ID, flag any user who
clicks the same ad more than k times within a rolling t second
window. Return flagged users in order of first violation.

Goal: sliding window or queue based approach, O(n) or O(n log n).
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Click:
    user_id: str
    ad_id: str
    timestamp: int  # seconds


def detect_click_fraud(clicks: List[Click], k: int, t: int) -> List[str]:
    """
    Return a list of user_ids flagged for clicking the same ad more
    than k times within any rolling t-second window, ordered by the
    timestamp of their first violation.

    Assume `clicks` is not necessarily sorted by timestamp.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    clicks = [
        Click("u1", "ad1", 0),
        Click("u1", "ad1", 2),
        Click("u1", "ad1", 4),
        Click("u1", "ad1", 20),
        Click("u2", "ad1", 1),
        Click("u2", "ad2", 2),
    ]

    # u1 clicks ad1 three times within a 10 second window (0, 2, 4) ->
    # flagged if k=2. u2 never exceeds k across either ad.
    flagged = detect_click_fraud(clicks, k=2, t=10)
    assert flagged == ["u1"]

    flagged_strict = detect_click_fraud(clicks, k=3, t=10)
    assert flagged_strict == []

    print("All basic checks passed.")
