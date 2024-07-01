# 实现判断一个数是不是回文数的函数
def is_palindrome(num):
    temp = num
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    return reversed_num == num
