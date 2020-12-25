def solution(n, words):
    for word in range(1, len(words)):
        if words[word][0] != words[word-1][-1] or \
            words[word] in words[:word]:
            return [(word%n)+1, (word//n)+1]
    else:
        return [0, 0]