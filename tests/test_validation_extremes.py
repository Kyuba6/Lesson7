from src.manager import Manager
from src.models import Parameters, Transfer
import pytest

def test_transfer_below_minimum_is_invalid():
    manager = Manager(Parameters(min_transfer=10.0, max_transfer=5000.0))

    transfer = Transfer(
        tenant="tenant-1",
        date="2025-01-01",
        settlement_year=2025,
        settlement_month=1,
        amount_pln=5.0,
        type="rent"
    )

    errors = manager.validate_transfer(transfer)
    assert "below minimum" in errors[0].lower()

def test_transfer_above_maximum_is_invalid():
    manager = Manager(Parameters(min_transfer=10.0, max_transfer=5000.0))

    transfer = Transfer(
        tenant="tenant-1",
        date="2025-01-01",
        settlement_year=2025,
        settlement_month=1,
        amount_pln=10000.0,
        type="rent"
    )

    errors = manager.validate_transfer(transfer)
    assert "above maximum" in errors[0].lower()

def test_transfer_within_range_is_valid():
    manager = Manager(Parameters(min_transfer=10.0, max_transfer=5000.0))

    transfer = Transfer(
        tenant="tenant-1",
        date="2025-01-01",
        settlement_year=2025,
        settlement_month=1,
        amount_pln=100.0,
        type="rent"
    )

    errors = manager.validate_transfer(transfer)
    assert errors == []