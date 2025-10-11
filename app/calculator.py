def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """Возвращает ежемесячный платёж по ипотеке."""
    if years <= 0:
        raise ValueError("Срок кредита должен быть положительным числом лет.")
    if principal <= 0:
        raise ValueError("Сумма кредита должна быть положительной.")
    if annual_rate < 0:
        raise ValueError("Ставка не может быть отрицательной).")

    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        return principal / months

    payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return round(payment, 2)