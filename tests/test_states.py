import pytest

@pytest.fixture
def first_state(states):
    return states[0]


@pytest.fixture
def last_state(states):
    return states[-1]


@pytest.fixture
def last_standard_state(states):
    return states[-2]


def test_states_body(first_state, last_state):
    assert last_state.body < first_state.body


def test_states_percentage(first_state, last_state):
    last_percentage_pay = last_state.month_percentage_pay
    first_percentage_pay = first_state.month_percentage_pay

    assert last_percentage_pay < first_percentage_pay


def test_states_body_pay(first_state, last_standard_state):
    last_standard_body_pay = last_standard_state.month_body_pay
    first_body_pay = first_state.month_body_pay

    assert last_standard_body_pay > first_body_pay


def test_states_pay(first_state, last_standard_state):
    last_standard_month_pay = last_standard_state.month_body_pay + last_standard_state.month_percentage_pay
    first_month_pay = first_state.month_body_pay + first_state.month_percentage_pay
    assert last_standard_month_pay == first_month_pay


def test_states_date(first_state, last_state):
    assert last_state.current_date > first_state.current_date


def test_last_state_body(last_state):
    assert last_state.new_body == 0
