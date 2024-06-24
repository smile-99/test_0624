#輸入: ‘417324689435’
#輸出: ‘975331244468'

# verifyInput
def verifyInput(n):
    if n.isdigit() == True:
        sortOddEvent(n)
    else:
        print("請重新執行並輸入 1-9 的數字")
        exit()

# 奇偶數、sort升降冪
def sortOddEvent(n):
    list_odd = []
    list_event = []
    for i in list(n):
        if ( int(i) % 2) != 0:
            list_odd.append(int(i))
        else:
            list_event.append(int(i))
    print(sorted(list_odd, reverse=True)+sorted(list_event,reverse=False))

# 截取輸入資料，整理成數字字串
n = input("輸入2個以上奇偶整數：")
verifyInput(n)