# this contain the base config for pytest
import pytest
from item.models import Buyer


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """fixture to execute asserts before and after a test is run"""

    from conf_test_db import override_get_db

    database = next(override_get_db())
    new_buyer = Buyer(name="max", email="max@gmail.com", password="123456")
    database.add(new_buyer)
    database.commit()
    yield  # this is where the testing happens
    database.query(Buyer).filter(Buyer.email == "max@gmail.com").delete()
    database.commit()
