#
#  lv2_스킬트리.py
#  스킬트리
#
#  Create by 김도영 on 2021/04/23
#


def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        list = [s.index(i) for i in skill if i in s]
        list_ = sorted(list)

        # "BDA"와 같은 경우 all() 조건이 필요
        # list == list_는 같지만 맨 처음 "C"가 없기 때문에 불가능
        # skill에서 앞 순서대로 있어야 한다. 중간 띄어넘기 불가
        if list == list_ and all(i in s for i in skill[: len(list)]):
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))