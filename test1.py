# 輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形

# 判斷輸入值是否為大於2的整數，若不符合提示錯誤
def estimateInput(n):
    if n.isdigit():
        if int(n) >= 2:
            printTriangle(int(n))
        else:
            print("請重新執行，並且輸入一個大於或等於2的整數")
            exit()
    else:
        print("請重新執行，並且輸入一個大於或等於2的整數")
        exit()

# 空心正三角形
def printTriangle(n):
    # 最上層
    print(" "*(n-1)+"*")
    # 中間層
    for i in range(1, n-1):
            print(" "*(n-i-1)+"*"+" "*(2*i-1)+"*")
    # 底層
    if n > 1:
            print(" ".join("*"*n))

# 截取輸入資料
n = input("輸入一個大於或等於2的整數：")
estimateInput(n)