from dataclasses import dataclass
from datetime import date
from functools import cached_property

from loancalc.constants import MONTH_IN_YEAR


@dataclass
class LoanInfo:
    body: float
    percentage: float
    time: int

    start_date: date

    @cached_property
    def year_percentage_rate(self):
        return self.percentage / 100

    @cached_property
    def month_percentage_rate(self):
        return self.year_percentage_rate / MONTH_IN_YEAR

    @cached_property
    def rate(self):
        rate = (1 + self.month_percentage_rate) ** self.time
        return (self.month_percentage_rate * rate) / (rate - 1)

    @cached_property
    def pay_month(self):
        return self.rate * self.body
