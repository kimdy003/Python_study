def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_dist = 2e9
        current, remove = 0, 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove += 1
                if remove > n:
                    break
            else:
                current = rock
                min_dist = min(min_dist, diff)

        if remove > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1

    return answer
