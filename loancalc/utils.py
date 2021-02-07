import itertools
from calendar import Calendar
from functools import partial

from loancalc.constants import MONTH_IN_YEAR


def days_in_month(year, month):
    return list(filter(None, Calendar().itermonthdays(year, month)))[-1]


def days_in_year(year):
    month_days_func = partial(Calendar().itermonthdays, year)

    year_days_iters = map(month_days_func, range(1, MONTH_IN_YEAR + 1))
    year_days_iter = itertools.chain(*year_days_iters)
    return len(list(filter(None, year_days_iter)))
