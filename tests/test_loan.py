import re
from typing import List

from loancalc import Loan

from loancalc.constants import REPORT_HEADER
from loancalc.loan_state import LoanState

REPORT_TEMPLATE = re.compile(r'^\s*(?P<pay_num>\d+)\s*\|'
                             r'\s*(?P<body>\d+(?:\.\d+))\s*\|'
                             r'\s*(?P<pay>\d+(?:\.\d+))\s*\|'
                             r'\s*(?P<percents>\d+(?:\.\d+))\s*\|'
                             r'\s*(?P<body_pay>\d+(?:\.\d+))\s*$')


def test_loan_report(loan: Loan, states: List[LoanState]):
    report = str(loan)
    header, *table = report.splitlines()

    assert header == REPORT_HEADER

    parsed_table = list(map(re.Match.groupdict, map(REPORT_TEMPLATE.match, table)))

    for i, states in enumerate(zip(states, parsed_table)):
        original_state, parsed_state = states

        assert int(parsed_state['pay_num']) == i
        assert float(parsed_state['body']) == round(original_state.new_body, 2)
        assert float(parsed_state['pay']) == round(original_state.pay, 2)
        assert float(parsed_state['percents']) == round(original_state.month_percentage_pay, 2)
        assert float(parsed_state['body_pay']) == round(original_state.month_body_pay, 2)


def test_loan_overpayment(loan):
    assert loan.overpayment > 0
