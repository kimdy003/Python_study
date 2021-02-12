def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()]    # 현재까지 고칠 수 있는 취약점들 저장
    count = 0
    dist.sort(reverse=True)

    # 고칠 수 있는 것들 리스트 작성
    for can_move in dist:
        repairs = []    # 친구 별 고칠 수 있는 취약점들 저장
        count += 1

        #수리 가능한 지점 찾기
        for i, wp in enumerate(weak):
            start = wp    # 각 워크포인트 시작
            ends = weak[i:] + [n+w for w in weak[:i]]    #시작점 기준 끝 포인트 값 저장
            can =[end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))

        cand = set()
        for r in repairs:
            for x in repair_lst:
                new = r | set(x)
                if len(new) == W:
                    return count
                cand.add(tuple(new))
        repair_lst = cand

    return -1

print(solution(12, [1, 5, 6, 10], [1,2,3,4]))