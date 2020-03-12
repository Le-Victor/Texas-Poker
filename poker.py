import numpy as np
import pytest

def kinds(num):             #牌型名对应数字
    if num == 1:
        return "High Card: "
    if num == 2:
        return "Pair"
    if num == 3:
        return "Two Pairs"
    if num == 4:
        return "Three of a kind"
    if num == 5:
        return "Straight"
    if num == 6:
        return "Flush"
    if num == 7:
        return "Full House"
    if num == 8:
        return "Four of a kind"
    if num == 9:
        return "Straight Flush"

def txtin(cards):               #将卡片输入到数组
    a = np.zeros((5, 2), dtype=np.str)
    i = 0
    j = 0
    for str in cards:
        if str != ' ':
            a[i][j] = str
            if j != 1:
                j+=1
            else:
                i+=1
                j = 0
    # print(a)
    return a

def change(str):                 #转换数字和字符
    if str == 'T':
        return 10
    if str == 'J':
        return 11
    if str == 'Q':
        return 12
    if str == 'K':
        return 13
    if str == 'A':
        return 14
    if str == 2:
        return '2'
    if str == 3:
        return '3'
    if str == 4:
        return '4'
    if str == 5:
        return '5'
    if str == 6:
        return '6'
    if str == 7:
        return '7'
    if str == 8:
        return '8'
    if str == 9:
        return '9'
    if str == 10:
        return "10"
    if str == 11:
        return "Jack"
    if str == 12:
        return "Queen"
    if str == 13:
        return "King"
    if str == 14:
        return "Ace"
    else:
        return int(str)

def swap(a,b):
    return b,a

def bubble(a):                  #冒泡排序
    for j in range(4,0,-1):
        for i in range(0,j):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a

def judge1(ints):       #判断是不是顺子
    i = 0
    j = 0
    while(i<4):
        if ints[i]+1 != ints[i+1]:
            break
        else:
            i+=1
    if i == 4:
        return 5        #顺子
    else:               #判断有几个对子
        while(j<4):
            if ints[j] != ints[j+1]:
                j+=1
            else:
                break
        if j == 4:
            return 1                #散牌
        if j == 3:
            return 2                #(3,4)对子
        if j == 2:
            if ints[3] != ints[4]:
                ints[2], ints[4] = swap(ints[2], ints[4])
                return 2            #(2,3)对子
            else:
                return 4            #(2,3,4)三条
        if j == 1:
            if ints[2] != ints[3]:
                if ints[3] != ints[4]:
                    ints[2], ints[4] = swap(ints[2], ints[4])
                    ints[1], ints[3] = swap(ints[1], ints[3])
                    return 2        #(1,2)对子
                else:
                    return 3        #(1,2)(3,4)两对
            else:
                if ints[3] != ints[4]:
                    ints[1], ints[4] = swap(ints[1], ints[4])
                    return 4        #(1,2,3)三条
                else:
                    return 8        #(1,2,3,4)铁支
        if j == 0:
            if ints[1] != ints[2]:
                if ints[2] != ints[3]:
                    if ints[3] != ints[4]:
                        ints[1], ints[4] = swap(ints[1], ints[4])
                        ints[0], ints[3] = swap(ints[0], ints[3])
                        ints[2], ints[1] = swap(ints[2], ints[1])
                        ints[1], ints[0] = swap(ints[1], ints[0])
                        return 2    # (0,1)对子
                    else:
                        ints[0], ints[2] = swap(ints[0], ints[2])
                        return 3    # (0,1)(3,4)两对
                else:
                    if ints[3] != ints[4]:
                        ints[2], ints[4] = swap(ints[2], ints[4])
                        ints[0], ints[2] = swap(ints[0], ints[2])
                        return 3    # (0,1)(2,3)两对
                    else:
                        return 7    # (0,1)(2,3,4)葫芦
            else:
                if ints[2] != ints[3]:
                    if ints[3] != ints[4]:
                        ints[0], ints[3] = swap(ints[0], ints[3])
                        ints[1], ints[4] = swap(ints[1], ints[4])
                        return 4    # (0,1,2)三条
                    else:
                        ints[4], ints[1] = swap(ints[4], ints[1])
                        ints[3], ints[0] = swap(ints[3], ints[0])
                        return 7    # (0,1,2)(3,4)葫芦
                else:
                    ints[4], ints[0] = swap(ints[4], ints[0])
                    return 8    # (0,1,2,3)铁支

def judge2(a, b, c, d, e):          #判断是否是同花
    if a == b and b == c and c == d and d == e:
        return 1
    else:
        return 0

def deal(side):                 #判断牌
    s =txtin(side)
    ints = np.zeros((5),dtype=int)
    for i in range(0,5):
        ints[i] = change(s[i][0])
    ints = bubble(ints)
    # print(ints)
    ans = judge1(ints)          #牌的结果
    if judge2(s[0][1], s[1][1], s[2][1], s[3][1], s[4][1]) == 1:
        if ans == 1:
            ans = 6  # 同花
        if ans == 5:
            ans = 9  # 同花顺
    # print(ans)
    # print(ints)
    return ans, ints

def compare(ansb, b, answ, w):
    if ansb > answ:         #Black嬴
        return "Black wins", kinds(ansb)
    if ansb < answ:         #White嬴
        return "White wins", kinds(answ)
    if ansb == answ:        #牌型相同
        if ansb == 5 or ansb == 9:   #顺子和同花顺比较最大牌
            if b[4] > w[4]:
                return "Black wins", kinds(ansb)
            if b[4] < w[4]:
                return "White wins", kinds(answ)
            else:
                return "Tie", kinds(ansb)
        if ansb == 4 or ansb == 7 or ansb == 8:         #三条，葫芦和铁汁同样大小的最大牌
            if b[4] > w[4]:
                return "Black wins", kinds(ansb)
            if b[4] < w[4]:
                return "White wins", kinds(answ)
            else:
                return "Tie", kinds(ansb)
        if ansb == 1:      #散牌依次比较牌的大小
            for i in range(4,-1,-1):
                if b[i] > w[i]:
                    return "Black wins", kinds(ansb)+change(b[i])
                if b[i] < w[i]:
                    return "White wins", kinds(answ)+change(w[i])
            return "Tie", kinds(ansb)+change(b[4])
        if ansb == 6:      #同花依次比较牌的大小
            for i in range(4,-1,-1):
                if b[i] > w[i]:
                    return "Black wins", kinds(ansb)
                if b[i] < w[i]:
                    return "White wins", kinds(answ)
            return "Tie", kinds(ansb)
        if ansb ==3:        #两对比较大对子，小对子，单牌
            if b[4] > w[4]:
                return "Black wins", kinds(ansb)
            if b[4] < w[4]:
                return "White wins", kinds(answ)
            else:
                if b[2] > w[2]:
                    return "Black wins", kinds(ansb)
                if b[2] < w[2]:
                    return "White wins", kinds(answ)
                else:
                    if b[0] > w[0]:
                        return "Black wins", kinds(ansb)
                    if b[0] < w[0]:
                        return "White wins", kinds(answ)
                    else:
                        return "Tie", kinds(ansb)
        if ansb ==2:        #比较对子，再比较剩下的单牌
            if b[4] > w[4]:
                return "Black wins", kinds(ansb)
            if b[4] < w[4]:
                return "White wins", kinds(answ)
            else:
                for j in range(2, -1, -1):
                    if b[j] > w[j]:
                        return "Black wins", kinds(ansb)
                    if b[j] < w[j]:
                        return "White wins", kinds(answ)
                return "Tie", kinds(ansb)

def main():
    black = input("Black:")          #输入Black牌
    ansb, b = deal(black)

    white = input("White:")         #输入White牌
    answ, w = deal(white)

    winner, poker = compare(ansb, b, answ, w)
    if winner != "Tie":
        print(winner + " - " + poker)
    else:
        print(winner)


if __name__ == '__main__':
    main()

def test_deal():
    a1, b1 = deal("2H 5D 3S KC 9D")
    assert a1 == 1
    assert all(b1 == [2, 3, 5, 9, 13])
    a2, b2 = deal("2H 4S 4C 2D 4H")
    assert a2 == 7
    assert all(b2 == [2, 2, 4, 4, 4])
    a3, b3 = deal("TH 4S 4C 2D 4H")
    assert a3 == 4
    assert all(b3 == [2, 10, 4, 4, 4])
    a4, b4 = deal("2H AS 4C 2D AH")
    assert a4 == 3
    assert all(b4 == [4, 2, 2, 14, 14])
    a5, b5 = deal("JH AS QC QD 3H")
    assert a5 == 2
    assert all(b5 == [3, 11, 14, 12, 12])
    a6, b6 = deal("7H TS JC 9D 8H")
    assert a6 == 5
    assert all(b6 == [7, 8, 9, 10, 11])
    a7, b7 = deal("2H AH 7H 3H 9H")
    assert a7 == 6
    assert all(b7 == [2, 3, 7, 9, 14])
    a8, b8 = deal("7H 7S KC 7D 7H")
    assert a8 == 8
    assert all(b8 == [13, 7, 7, 7, 7])
    a9, b9 = deal("AS TS QS JS KS")
    assert a9 == 9
    assert all(b9 == [10, 11, 12, 13, 14])

def test_compare():
    a1, b1 = compare(1, [2, 4, 7, 9, 11], 1, [3, 5, 6, 7, 11])
    assert a1 == "Black wins"
    assert b1 == "High Card: 9"
    a2, b2 = compare(1, [2, 4, 7, 9, 11], 1, [3, 5, 6, 7, 14])
    assert a2 == "White wins"
    assert b2 == "High Card: Ace"
    a3, b3 = compare(1, [3, 5, 6, 7, 12], 1, [3, 5, 6, 7, 12])
    assert a3 == "Tie"
    assert b3 == "High Card: Queen"
    a4, b4 = compare(8, [3, 5, 5, 5, 5], 8, [11, 5, 5, 5, 5])
    assert a4 == "Tie"
    assert b4 == "Four of a kind"
    a4, b4 = compare(9, [3, 4, 5, 6, 7], 8, [11, 5, 5, 5, 5])
    assert a4 == "Black wins"
    assert b4 == "Straight Flush"
    a5, b5 = compare(3, [11, 4, 4, 6, 6], 3, [3, 2, 2, 5, 5])
    assert a5 == "Black wins"
    assert b5 == "Two Pairs"
    a6, b6 = compare(3, [11, 4, 4, 10, 10], 3, [3, 7, 7, 10, 10])
    assert a6 == "White wins"
    assert b6 == "Two Pairs"
    a7, b7 = compare(3, [5, 7, 7, 10, 10], 3, [5, 7, 7, 10, 10])
    assert a7 == "Tie"
    assert b7 == "Two Pairs"
    a8, b8 = compare(3, [5, 7, 7, 10, 10], 3, [14, 7, 7, 10, 10])
    assert a8 == "White wins"
    assert b8 == "Two Pairs"
    a9, b9 = compare(2, [5, 7, 14, 10, 10], 2, [3, 6, 7, 10, 10])
    assert a9 == "Black wins"
    assert b9 == "Pair"
    a10, b10 = compare(2, [5, 7, 8, 11, 11], 2, [3, 6, 14, 10, 10])
    assert a10 == "Black wins"
    assert b10 == "Pair"
    a11, b11 = compare(2, [5, 7, 8, 11, 11], 2, [5, 7, 8, 11, 11])
    assert a11 == "Tie"
    assert b11 == "Pair"
    a12, b12 = compare(2, [5, 7, 8, 11, 11], 9, [5, 6, 7, 8, 9])
    assert a12 == "White wins"
    assert b12 == "Straight Flush"
    a13, b13 = compare(2, [5, 7, 8, 11, 11], 1, [5, 6, 7, 8, 14])
    assert a13 == "Black wins"
    assert b13 == "Pair"
    a13, b13 = compare(4, [5, 7, 11, 11, 11], 4, [3, 14, 9, 9, 9])
    assert a13 == "Black wins"
    assert b13 == "Three of a kind"

