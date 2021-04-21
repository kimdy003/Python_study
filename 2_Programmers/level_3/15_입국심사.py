def solution(n, times):
    faster = min(times)

    start = faster
    end = n * faster
    min_time = n * faster

    while start <= end:
        mid = (start+end)//2
        check = 0

        for time in times:
            check += (mid // time)
            if check >= n:
                min_time = mid
                end = mid -1
                break
        
        if check < n:
            start = mid + 1

    return min_time

print(solution(6, [7, 10]))