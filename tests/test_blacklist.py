from src.manager import Manager
from src.models import Parameters, BlacklistedTenant

def test_blacklisted_tenant_is_detected():
    manager = Manager(Parameters())
    manager.blacklist = {
        "Jan Kowalski": BlacklistedTenant(
            name="Jan Kowalski",
            reason="Unpaid rent"
        )
    }

    assert manager.is_blacklisted("Jan Kowalski") is True

def test_non_blacklisted_tenant_is_not_detected():
    manager = Manager(Parameters())
    manager.blacklist = {}

    assert manager.is_blacklisted("Adam Nowak") is False
