import numpy as np

#定義複利計算函数
def compound_interest(principal, rate, time, n):
    # 將年利率��換為月利率
    monthly_rate = rate / 12

    # 計算每月的複利
    amount = principal * (1 + monthly_rate / n) ** (n * time)

    # 計算每月的複利金��
    monthly_interest = amount - principal

    return monthly_interest

principal = 20000
rate = 0.03
time = 10  # 1 個年
n = 12  # 按月計算

print(compound_interest(principal, rate, time, n))