from src.manager import Manager
from src.models import Parameters, Transfer
import pytest

def test_transfer_with_unknown_tenant_is_flagged():
    manager = Manager(Parameters())
    manager.tenants = {}  # brak najemców

    transfer = Transfer(
        tenant="ghost",
        date="2025-01-01",
        settlement_year=2025,
        settlement_month=1,
        amount_pln=100.0,
        type="rent"
    )

    errors = manager.check_transfer_errors(transfer)
    assert "unknown tenant" in errors[0].lower()

def test_transfer_outside_agreement_dates_is_flagged():
    manager = Manager(Parameters())
    tenant = list(manager.tenants.values())[0]

    transfer = Transfer(
        tenant=tenant.key,
        date="2030-01-01",  # poza umową
        settlement_year=2030,
        settlement_month=1,
        amount_pln=100.0,
        type="rent"
    )

    errors = manager.check_transfer_errors(transfer)
    assert "outside agreement" in errors[0].lower()
