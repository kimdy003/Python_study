def solution(enroll, referral, seller, amount):
    def bottomUp(sell, price):
        if sell == "center":
            ret[sell] += price
            return

        upPrice = int(price * 0.1)
        ret[sell] += price - upPrice
        if upPrice:
            bottomUp(tree[sell], upPrice)

    ret, tree = {roll: 0 for roll in ["center"] + enroll}, {}
    for e, r in zip(enroll, referral):
        tree[e] = "center" if r == "-" else r

    for sell, amt in zip(seller, amount):
        price = amt * 100

        bottomUp(sell, price)
        print(ret)

    return [ret[roll] for roll in enroll]


print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
    )
)
# print(
#     solution(
#         ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#         ["sam", "emily", "jaimie", "edward"],
#         [2, 3, 5, 4],
#     )
# )
