from datetime import date

from loancalc import Loan


def test_loan():
    loan = Loan(body=1000000, percentage=10.7, time=120, initial_date=date(2020, 12, 1))
    print(loan)
