#实现判断一个数是不是素数的函数

def is_prime(num):
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