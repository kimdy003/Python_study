import re
from collections import defaultdict


def solution(word, pages):
    urlToIdx = defaultdict(int)
    urlToScore = defaultdict(list)
    urlToExlink = defaultdict(list)
    word = word.lower()

    for i in range(len(pages)):
        lp = pages[i].lower()
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>', lp).group(1)
        urlToIdx[url] = i
        # print(url)  # a.com, b.com, c.com
        wordCnt = 0

        for find in re.findall(r"[a-zA-Z]+", lp):
            # print(find)  # 영문자들만. 즉, 단어별 나누기
            if find == word:
                wordCnt += 1

        s = set()
        for e in re.findall(r'<a href="https://[\S]*">', lp):
            s.add(re.search(r'"https://([\S]*)"', e).group(1))

        s = list(s)
        urlToScore[url].append(wordCnt)
        urlToScore[url].append(len(s))

        for e in s:
            urlToExlink[e].append(url)

    result = []
    for k, v in urlToScore.items():
        score = v[0]
        if k in urlToExlink:
            for u in urlToExlink[k]:
                score += urlToScore[u][0] / urlToScore[u][1]
        result.append([score, urlToIdx[k]])

    return sorted(result, key=lambda x: [-x[0], x[1]])[0][1]


print(
    solution(
        "blind",
        [
            '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
            '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
            '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
        ],
    )
)
