from typing import Tuple


def get_interest(principal: int, num_days: int) -> int:
    INTEREST_RATE = 0.02
    DAYS_PER_YEAR = 365
    return round(principal * INTEREST_RATE * num_days / DAYS_PER_YEAR - 0.5)


def get_interest_income_tax(interest: float) -> int:
    INTEREST_INCOME_TAX_RATE = 0.14
    return round(interest * INTEREST_INCOME_TAX_RATE - 0.5)


def get_residence_tax(interest_income_tax: int) -> int:
    RESIDENCE_TAX_RATE = 0.1
    return round(interest_income_tax * RESIDENCE_TAX_RATE - 0.5)


def get_total(start_value: int, intervals: Tuple[int]):
    error_message: str = 'Invalid intervals. Remember that interest is always paid on the third Saturday.'
    assert sum(intervals) in [28, 35], error_message
    for interval in intervals:  # interval: int
        interest: int = get_interest(start_value, interval)
        interest_income_tax: int = get_interest_income_tax(interest)
        residence_tax: int = get_residence_tax(interest_income_tax)
        start_value += interest - interest_income_tax - residence_tax
    return start_value


if __name__ == '__main__':
    for start_value in [
        1000000,
        2000000,
        3000000,
        5000000,
        10000000,
    ]:
        print(f'If you start with {start_value:,}:')
        for intervals in [
            (1,) * 28,
            (2,) * 14,
            (4,) * 7,
            (7,) * 4,
            (14,) * 2,
            (28,) * 1,
        ]:
            total: int = get_total(start_value, intervals)
            print(f'{total:,} <--- {intervals}')
