def mortgage_payment(principal: float, rate: float, years: int) -> float:
    """Вычисляет ежемесячный платёж по ипотеке."""
    monthly_rate = rate / 100 / 12
    months = years * 12
    return principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
