import re


def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    lst = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    return ["".join(s) for s in lst]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
