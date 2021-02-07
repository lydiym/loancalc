from datetime import date
from random import randint

import pytest

from loancalc import Loan


@pytest.fixture
def loan():
    return Loan(body=randint(10 ** 4, 10 ** 7),
                percentage=randint(1, 99),
                time=randint(12, 12 * 40),
                initial_date=date.today())


@pytest.fixture
def states(loan):
    return list(loan.states())

