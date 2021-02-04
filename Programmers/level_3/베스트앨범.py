def solution(genres, plays):
    answer = []
    dic = {}
    total = {}

    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [(plays[i], i)]
            total[genres[i]] = plays[i]
        else:
            dic[genres[i]].append((plays[i], i))
            total[genres[i]] += plays[i]

    total = sorted(total.items(), key=lambda x:x[1], reverse=True)

    for key in total:
        play_list = dic[key[0]]
        play_list = sorted(play_list, key=lambda x:(-x[0], x[1]))

        for i in range(len(play_list)):
            if i == 2:
                break;
            answer.append(play_list[i][1])

    return answer

# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     print("----")
#     print(genreSort)
#     print("----")

#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (-x[0], x[1]))]
#         #print(temp)
#         answer += temp[:min(len(temp),2)]
#     return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))