from app.calculator import calculate_monthly_payment


def test_basic_calculation():
    assert calculate_monthly_payment(1_000_000, 10, 20) == 9650.22


def test_zero_rate():
    assert calculate_monthly_payment(1_200_000, 0, 10) == 10000.0


def test_invalid_values():
    from pytest import raises
    with raises(ValueError):
        calculate_monthly_payment(-500_000, 10, 15)
