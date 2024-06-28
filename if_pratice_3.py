"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: Johnson
"""

value = float(input("Value = "))
unit = input("Unit = ")
if unit == "in" or unit == "英寸":
    print("%.2f英寸 = %.2f厘米" % (value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("%.2f厘米 = %.2f英寸" % (value, value / 2.54))
else:
    print("请输入有效的单位")