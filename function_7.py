#写一个程序判断输入的正整数是不是回文素数。

if __name__ == '__main__':
    num = int(input("请输入一个正整数: "))
    temp = num
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    if reversed_num == num:
        print("%d是回文数" % num)
    else:
        print("%d不是回文数" % num)
    end = int(num ** 0.5)
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print("%d是素数" % num)
    else:
        print("%d不是素数" % num)