from datetime import date
from functools import cached_property
from itertools import starmap

from dateutil.relativedelta import relativedelta

from loancalc.constants import LOAN_REPORT_ROW_TEMPLATE, REPORT_HEADER
from loancalc.loan_info import LoanInfo
from loancalc.loan_state import LoanState


class Loan:
    def __init__(self, body: float, percentage: float, time: int, initial_date: date):
        self.info = LoanInfo(body, percentage, time, initial_date)

    def states(self):
        last_state = LoanState(self.info, self.info.body, self.info.start_date)
        yield last_state

        while last_state.new_body > 0:
            body = last_state.new_body
            new_date = last_state.current_date + relativedelta(months=+1)

            last_state = LoanState(self.info, body, new_date)
            yield last_state

    def _month_report(self):
        def report_format(num: int, state: LoanState):
            return LOAN_REPORT_ROW_TEMPLATE.format(
                payment_num=num,
                body=round(state.new_body, 2),
                pay=round(state.pay, 2),
                percentage_pay=round(state.month_percentage_pay, 2),
                body_pay=round(state.month_body_pay, 2)
            )

        return REPORT_HEADER + '\n' + '\n'.join(starmap(report_format, enumerate(self.states())))

    @cached_property
    def overpayment(self):
        return self.info.pay_month * self.info.time - self.info.body

    def __str__(self):
        return self._month_report()
