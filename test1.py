# 判斷輸入值是否為大於2的整數，若不符合提示錯誤
def input_estimate(n):
    if n >= 2:
        print_triangle(n)
    else:
        print("請重新執行，並且輸入一個大於或等於2的整數")

# 空心正三角形
def print_triangle(n):
    # 最上層
    print(" "*(n-1)+"*")
    # 中間層
    for i in range(1, n-1):
            print(" "*(n-i-1)+"*"+" "*(2*i-1)+"*")
    # 底層
    if n > 1:
            print(" ".join("*"*n))

# 截取輸入資料
n = int(input("輸入一個大於或等於2的整數："))
input_estimate(n)