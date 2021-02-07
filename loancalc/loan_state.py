from dataclasses import dataclass
from datetime import date
from functools import cached_property

from loancalc.constants import LOAN_STATE_TEMPLATE
from loancalc.loan_info import LoanInfo
from loancalc.utils import days_in_month, days_in_year


@dataclass
class LoanState:
    info: LoanInfo
    body: float

    current_date: date

    @cached_property
    def _days_between_dates(self):
        # TODO should calculate truly days between dates. See specification
        return days_in_month(self.current_date.year, self.current_date.month)

    @cached_property
    def month_percentage_pay(self):
        days_in_current_year = days_in_year(self.current_date.year)
        pay = self.body * self.info.year_percentage_rate * self._days_between_dates / days_in_current_year
        if pay < 0:
            print(pay)
        return pay

    @cached_property
    def month_body_pay(self):
        if self.body > self.info.pay_month:
            return self.info.pay_month - self.month_percentage_pay

        return self.body - self.month_percentage_pay

    @cached_property
    def pay(self):
        return self.month_body_pay + self.month_percentage_pay

    @cached_property
    def new_body(self):
        return self.body - self.pay

    def __str__(self):
        return LOAN_STATE_TEMPLATE.format(body=round(self.new_body, 2),
                                          pay=round(self.pay, 2),
                                          percentage_pay=round(self.month_percentage_pay, 2),
                                          body_pay=round(self.month_body_pay, 2))
