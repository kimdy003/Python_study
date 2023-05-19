def prime_list(N):
    # 에라토스테네스의 체 초기화
    # 0, 1 = [False] + (n-2)개의 요소 True => len(sieve) = N + 1
    sieve = [False, False] + [True] * (N - 1)

    M = int(N**0.5)  # 루트 N개까지만 해도 된다.시간단축
    for i in range(2, M + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, N + 1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(N + 1) if sieve[i] == True]


print(len(prime_list(500000)))
