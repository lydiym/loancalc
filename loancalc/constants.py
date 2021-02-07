MONTH_IN_YEAR = 12
LOAN_STATE_TEMPLATE = '{body:<15}|{pay:<15}|{percentage_pay:<15}|{body_pay:<15}'
LOAN_REPORT_ROW_TEMPLATE = '{payment_num:<10}|' + LOAN_STATE_TEMPLATE

REPORT_HEADER = LOAN_REPORT_ROW_TEMPLATE.format(
    payment_num='Payment №',
    body='Remaining body',
    pay='Payment',
    percentage_pay='% payment',
    body_pay='Body payment'
)
