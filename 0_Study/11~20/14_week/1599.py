import sys

input = sys.stdin.readline

eng = [chr(i) for i in range(97, 117)]
mansic = [
    "a",
    "b",
    "k",
    "d",
    "e",
    "g",
    "h",
    "i",
    "l",
    "m",
    "n",
    ".",  # ng
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "y",
]

arr, dic = [], {}
N = int(input())
for _ in range(N):
    word = input().strip()
    temp = word.replace("ng", ".")

    change = ""
    for s in temp:
        change += eng[mansic.index(s)]

    arr.append(change)
    dic[change] = word

arr.sort()
for a in arr:
    print(dic[a])
