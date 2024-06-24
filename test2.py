# 奇偶數、sort升降冪
def sort_odd_event(n):
    list_odd = []
    list_event = []
    for i in n:
        if ( int(i) % 2) != 0:
            list_odd.append(int(i))
        else:
            list_event.append(int(i))
    print(sorted(list_odd, reverse=True)+sorted(list_event,reverse=False))

# 截取輸入資料，整理成數字字串
n = list(input("輸入2個以上奇偶整數："))
sort_odd_event(n)

#輸入: ‘417324689435’
#輸出: ‘975331244468'