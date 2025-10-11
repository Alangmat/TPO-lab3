import tkinter as tk
from tkinter import messagebox
from app.calculator import calculate_monthly_payment

def calculate():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        years = int(entry_years.get())
        payment = calculate_monthly_payment(principal, rate, years)
        label_result.config(text=f"Ежемесячный платёж: {payment:.2f} ₽")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Ипотечный калькулятор")
root.geometry("350x250")

tk.Label(root, text="Сумма кредита (₽):").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Процентная ставка (%):").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Срок (лет):").pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text="Рассчитать", command=calculate).pack(pady=10)
label_result = tk.Label(root, text="Ежемесячный платёж: —")
label_result.pack()

root.mainloop()