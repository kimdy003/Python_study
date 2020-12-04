#구명보트

def solution(people, limit):
    answer = 0
    people.sort()
    
    front = 0
    back = len(people)-1
    while back - front >= 1:
        if people[front]+people[back] <= limit:
            front += 1
            back -= 1
        else:
            back -= 1
        answer += 1
    if front == back:
        answer += 1
    
    return answer