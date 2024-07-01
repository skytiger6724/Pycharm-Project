# 打印[杨辉三角](https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2)。
def main():
    row = int(input("请输入行数: "))
    for i in range(row):
        for _ in range(row - i - 1):
            print(" ", end="")
        for _ in range(2 * i + 1):
            print("*", end="")
        print()

if __name__ == '__main__':
    main()