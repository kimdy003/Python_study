import sys

input = sys.stdin.readline

_input = input().strip()
card = {"P": [], "K": [], "H": [], "T": []}

for i in range(0, len(_input), 3):
    num = int(_input[i + 1 : i + 3])
    if num in card[_input[i]]:
        print("GRESKA")
        break
    else:
        card[_input[i]].append(num)
else:
    ans = []
    for lst in card.values():
        ans.append(str(13 - len(lst)))
    print(" ".join(ans))
