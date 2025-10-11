import pytest
from app.calculator import mortgage_payment

def test_mortgage_payment_basic():
    result = mortgage_payment(1_000_000, 10, 20)
    assert round(result, 2) == 9650.22  # Проверка на точность результата

def test_mortgage_payment_zero_rate():
    result = mortgage_payment(1_000_000, 0, 10)
    assert result == 1_000_000 / (10 * 12)
