def solution(S):
    answer = 0
    Max = int(240 * (2**10))
    cand = ["zip", "rar", "tgz"]

    S = S.split()
    lst = []
    for i in range(0, len(S) - 2, 3):
        if int(S[i + 1]) < Max:
            name, type = S[i + 2].split(".")
            if type in cand:
                year, mon, day = S[i].split("-")
                date = year + mon + day
                if int(date) < 19951013:
                    lst.append([S[i], S[i + 1], S[i + 2]])
                    answer += 1

    print(lst)
    return str(answer) if answer != 0 else "NO FILES"


print(
    solution(
        "1988-08-29        956 system.zip 1976-09-16     126976 old-photos.tgz 1987-02-03     118784 logs.rar 1961-12-04  703594496 very-long-filename.rar 1980-08-03          2 DELETE-THIS.TXT 2014-08-23        138 important.rar 2001-08-26     595968 MOONLIGHT-SONATA.FLAC 1967-11-30     245760 archive.rar 1995-10-13        731 file.tgz"
    )
)
