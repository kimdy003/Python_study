# 💡 데일리*알고리즘*풀이 - python 💡✔️

## 파이썬 다양한 입력방법(input(), readlline())

### 💡input()

```python
str = input()
num = int(input())
```

기본적인 입력 방법으로, input() 자체는 문자열을 입력받는 것으로 처리된다.  
그렇기 때문에 int(input())을 해주어야 숫자형 입력이 가능

<br/>

### num 변수에 저장된 숫자, 예를 들어 1993이란 숫자를 각각 하나씩 쪼개고 싶을 땐

```python
num = list(str(num))
print(num)    # ['1', '9', '9', '3']
```

<br/>

### 💡 input().split()

split() 내장함수는 문자열을 특정 구분자로 나누고 싶을 때 사용  
가령 split(',')은 쉼표로 구분된 문자열을 나눌 때 사용하면 된다  
split()는 공백으로 되어있으니 띄어쓰기를 구분

```python
str = input().split()
#  ['you', 'are', 'welcome']
```

<br/>

### 💡 map()

위의 input().split()은 하나의 변수에 리스트의 형태로 저장  
여러 변수를 생성하여 각각의 값을 할당하고 싶을 땐 map() 함수를 이용

주의할 점은 map() 함수는 최소한 2개의 인자를 괄호안에 써주어야한다.

```python
map(int, input().split())    # 숫자형을 입력받겠다.
map(str, input().split())    # 문자형을 입력받겠다.
```

<br/>

### 💡 sys.stdin.readline()

대량의 데이터를 반복적으로 입력받아야 할 때, input() 대신 sys.stdin.readline()을 이용하면 속도가 향상된다.  
주로 백준 저지 사이트에서 사용

```python
from sys import stdin
read = stdin.readline().split()
print(read)   # ['123', '345', '456'] str형태로 저장
```

하나의 변수에 list 형태로 저장

```python
import sys
y, m, d = map(int, sys.stdin.readline().split())
print(y, m, d)    # 1993 7 21
```

<br>

### 💡 배열

-   1차원 배열

```python
a = [0 for _ in range(5)]
print(a)    # [0, 0, 0, 0, 0]
```

-   2차원 배열

```python
m, n = 5, 4
a = [[0]*m for _ in range(n)]
print(a)    #[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
```

<br>

### 💡 for문을 이용한 N번 입력

```python
answer = [int(input()) for _ in range(N)]
```

<hr>

## heap - 힙

```python
import heapq # 기본은 min-heap, max-heap 사용시 -값 넣기

lst = [1, 2, 3]
heapq.heapify(lst)
# 빈 배열은 push시 자동으로 힙으로 됨
empty = []
```

<br/>

#### 💡 삽입 / 제거 / 조회

```python
heapq.heappop(my_list)
heapq.heappush(my_list, -1)
my_list[0]
```

<hr>

## queue - 큐

```python
from collections import deque
que = deque([1, 2, 3])
```

<br/>

#### 💡 원소 중간 삽입

```python
que.insert(i, num)
```

<br/>

#### 💡 삽입 / 제거 / 조회

```python
que.append(item)
que.popleft()
que[0]
```

<hr>

## counter

```python
import collections
my_list = ["a", "a", "b", "b", "c"]
collections.Counter(my_list)    # value 기준 정렬도 해줌

# Counter({'a': 2, 'b': 2, 'c': 1})
```

<hr>

## itertools

```python
import itertools
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import chain
```

<hr>

### 💡 파이썬의 재귀 깊이를 늘리는 코드

```python
import sys
sys.setrecursionlimit(10**6)
```

<br/>

### 💡 permutations - 순열

```python
permutations(range(1, 10), 3)
permutations(lst)
```

<br/>

### 💡 combinations - 조합

```python
combinations('ABC', 2)
```

<br/>

### 💡 product - 곱집합

두 개 이상의 리스트의 모든 조합을 구할때 사용
각 리스트에서 하나씩 뽑아서 조합을 만든다. 크기는 리스트 개수

```python
product(range(1,n1+1), range(1,n2+1), range(1,n3+1))

or_not = [(0, 500), (0, 1500)]
list(product(*or_not))

#[(0,0), (0,1500), (500,0), (500,1500)]
```

<br/>

### 💡 chain - flatten(2차배열 ->1차배열)

```python
itertools.chain(*board)
chain(*board)
```

<hr>

## dictionary - 해시

#### 💡 get

```python
my_dict['total']
my_dict.get('total', 0)
```

<br/>

#### 💡 제거 - pop : 키가 없는 경우 default 리턴

```python
my_dict.pop('홍길동', 180)
```

<br/>

#### 💡 탐색

```python
dict.items()
dict.keys()
dict.values()
```

<br/>

#### 💡 그래프 셋팅 : get 사용

```python
nodes = {}
for v1, v2 in edge:
    nodes[v1] = nodes.get(v1, []) + [v2]
    nodes[v2] = nodes.get(v2, []) + [v1]
```

<br/>

#### 💡 그래프 셋팅 with dist : get 사용

```python
nodes = {}
for v1, v2, d in road:
    nodes[v1] = nodes.get(v1, []) + [(v2, d)]
    nodes[v2] = nodes.get(v2, []) + [(v1, d)]
```

<br/>

#### 💡 그래프 셋팅 거리 초기화

```python
dist = { i:float('inf') if i != 1 else 0 for i in range(1, N+1) }
```

<hr>

## defaultdict

```python
from collections import defaultdict

dict1 = defaultdict(set)
dict2 = defaultdict(list)
dict3 = defaultdict(int) # -> 0으로 셋팅
```

<br/>

#### 💡 그래프 셋팅 : defaultdict 사용

```python
from collections import defaultdict
nodes = defaultdict(list)
for v1, v2 in edge:
    nodes[v1].append(v2)
    nodes[v2].append(v1)
```

<hr>

## set - 셋

#### 💡 삽입 / 제거

```python
my_set.add(3)
my_set.remove(3)
```

<br/>

#### 💡 include

```python
if 3 in my_set:
	print('3 있음')
if 3 not in my_set:
	print('3 없음')
```

<br/>

#### 💡 합집합, 교집합, 차집합

```python
set1 | set2
set1.update(set2)

set1 - set2

set1 & set2
```

<hr>

## bisect

```python
from bisect import bisect_left, bisect_right
```

<br/>

#### 💡 최소값 바로 왼쪽 (최소값 들어갈 index)

```python
bisect_left(lst, start)
```

<br/>

#### 💡 최대값 바로 오른쪽 (최대값 들어갈 index)

```python
bisect_right(lst, end)
```

<br/>

#### 💡 count_by_lange

```python
def count_by_lange(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)
```

<hr>

## DELTA - 방향

```python
DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 오른쪽 왼쪽 위 아래
DELTAS = [(-1, 0, UP), (1, 0, DOWN), (0, 1, RIGHT), (0, -1, LEFT)]
DELTAS = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}

DELTAS = {'U': (-1, -1), 'D': (1, 0), 'R': (0, 1)}
NEXT = {'U': 'D', 'D': 'R', 'R': 'U'}
```

<hr>

## visitable - 탐색 범위 확인

```python
def visitable(y, x, m, n):
    return 0 <= y < m and 0 <= x < n
```

<hr>

## 소수

```python
N, primes = end_num, set()
prime_check = [False, False] + [True]*(N-1)

for i in range(2, N+1):
    if prime_check[i]:
        primes.add(i)
        prime_check[i*2::i] = [False] * len(prime_check[i*2::i])
```

<hr>

## 최소공배수 / 최대공약수

#### 💡 최대공약수

```python
from fractions import gcd
gcd(6,8) # 2
```

<br/>

#### 💡 최소공배수

```python
def lcm(a,b):
    return  a * b // gcd(a, b)
```

<hr>

## 곱으로 나타내기

```python
[(number//i, i) for i in range(1, int(number**.5)+1) if number % i == 0]
# number = 24 -> 곱해서 24가되는 경우
[(24, 1), (12, 2), (8, 3), (6, 4)]
```

<hr>

## 이분탐색

#### 💡 최소값

```python
def impossible(n, middle, times):
    return sum([middle // x for x in times]) < n

def solution(n, times):
    left, right = 1, max(times)*n
    while left < right:
        middle = (left + right) // 2
        if impossible(n, middle, times):
            left = middle + 1
        else:
            right = middle
    return left
```

<br/>

#### 💡 최대값

```python
def is_poss(middle, budgets, M):
    return M >= sum([min(middle, budget) for budget in budgets])

def solution(budgets, M):
    left, right = 1, max(budgets)
    while left < right:
        middle = (left + right + 1) // 2
        if is_poss(middle, budgets, M):
            left = middle
        else:
            right = middle - 1
    return right
```

<hr>

## sort

#### 💡 sort

```python
lst.sort()
dist.sort(reverse=True)
lst.sort(key= lambda x : (x*4)[:4], reverse=True)
```

<br/>

#### 💡 sorted

```python
sorted(lst)
sorted(lst, reverse=True)
sorted(answer, key = lambda x : (x[0], -x[1], x[2]))

#Dictionary 정렬
dic = {}
sorted(dic)    # key 기준 정렬
sorted(dic, key=lambda x : dic[x])    # value 기준 정렬
```

<hr>

## count

#### 💡 요소 개수 세기

```python
lst.count(0)
[*row, *col, *diag].count(n)
```

<br/>

#### 💡 filter count

```python
filter = [item for item in items if 조건식 ]
len(filter)
```

<hr>

## 2차배열

#### 💡 초기화 m \* n 행렬

```python
board = [[0] * n for i in range(m)]

board = [[0]*n]*n   # 이 경우 n개의 [0]*n은 모두 같은 객체로 인식
```

<br/>

#### 💡 행열 뒤집기 (n\*m)

```python
reversed = list(map(list,zip(*board)))
```

<br/>

#### 💡 90도 회전

```python
def rotate90(arr):
    return list(zip(*arr[::-1]))
```

<hr>

## string

#### 💡 글자 replace

```python
query.replace('?','a')
```

<br/>

#### 💡 기준으로 쪼개기

```python
s.split("},{")
```

<br/>

#### 💡 join

String 형에서만 가능

```python
number = int(''.join(x))
```

list가 int인 경우

```python
lst = [1,2,2,3,4]
''.join(map(str, lst))
```

<br/>

#### 💡 string 갯수 단위로 쪼개기

```python
splited = [s[i:i+size] for i in range(0, LENGTH, size)]
# size = 3 : aabbaccc -> ['aab', 'bac', 'cc']
```

<hr>

## 정규식

```python
import re
```

<br/>

#### 💡 찾기

```python
re.search("^"+pre+".+",number)
re.findall(query, word)
lst = re.findall('\d+',s)
# ['2', '2', '1', '3', '4']
re.compile("(\D)")
```

<hr>

## 원형 선형으로

```python
weak_point = weak + [w+n for w in weak]
```

<hr>

## math

```python
import math
```

<br/>

#### 💡 ceil

```python
math.ceil(num / div)
```

<br/>

#### 💡 factorial

```python
math.factorial(3)
```

<hr>

## Exception 만들기

```python
try:
    if '에러 조건'
        raise EmptyException

except EmptyException:
    return False
```

```python
class EmptyException(Exception):
    pass
```

위처럼 파이썬의 내장 클래스인 Exception을 상속받으면 오류를 직접 만들 수 있다.

<hr>

## 아스키 코드 <-> 숫자 변환 방법

ord(문자) : 아스키 코드를 반환  
chr(숫자) : 숫자에 맞는 아스키 코드를 반환

<hr>

## 파이썬 시계 방향 회전 알고리즘

### 💡 90도 회전

```python
for r in range(N):
    for c in range(N):
        ret[c][N-1-r] = key[r][c]
```

회전 전의 열 번호와 회전 후의 행 번호가 일치  
그리고 회전 후의 열은 N-1에서 회전 전의 행을 뺀 값이다

<br/>

### 💡 180도 회전

```python
for r in range(N):
    for c in range(N):
        ret[N-1-r][N-1-c] = key[r][c]
```

회전 후의 행 번호는 N-1 의 값에서 전의 행 번호를 뺀 것과 같다.  
회전 후의 열 번호는 N-1 의 값에서 전의 열 번호를 뺀 것과 같다.

<br/>

### 💡 270도 회전

```python
for r in range(N):
    for c in range(N):
        ret[N-1-c][r] = key[r][c]
```

회전 후의 열과 전의 행이 일치한다.  
후의 행 번호는 N-1 에서 전의 열 번호를 뺀 값과 일치한다.

<br/>

### 💡파이썬 기반 회전 코드

```python
list(zip(*arr[::-1])) # 시계방향

list(reversed(list(zip(*arr)))) # 반시계방향
```
