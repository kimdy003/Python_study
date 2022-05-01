
# 💡 파이썬 모듈 사용설명서 💡✔️

## 💡'is'와 '=='의 차이
`is`와 `==`는 모두 변수의 동등을 비교하지만 다음과 같은 차이점이 있습니다.
* `is`는 변수의 Object(객체)가 같을 때 True를 리턴
* `==`는 변수의 Value(값)이 같을 때 True를 리턴
<hr><br>

## 💡!ln
하드 링크 또는 심볼릭 링크를 생성하는 명령어. 명령 실행 시 옵션 없이 사용하면 하드 링크가 생성되고, -s 옵션을 사용하면 심볼릭 링크를 생성  
### $ **ln [option] 원본 파일 대상명**
```
-s, --symbolic  
    심폴릭 링크를 생성 시에 사용하는 옵션

```
<br>

## colab 심폴릭 링크
그냥 drive에 폴더가 많을 경우 mount를 했을때 내가 원하는 폴더를 찾기가 어렵다 (가독성이 떨어짐)  
따라서 심폴릭 링크(ln)을 사용하여 내가 원하는 폴더만 가져와 경로를 새로 만들어 줄 수 있다.
``` python
# colab 사용 예시
from google.colab import drive

drive.mount('/gdrive')
!ln -s {원래 경로} {심폴릭 경로}
``` 
<hr>
<br>

## 💡파일 압축하기
### $ **zip [(저장 경로/)압축 파일명].zip [옵션] [압축할 파일명1][압축할 파일명2]...**
```
-r recurce of directory
    하위 디렉토리를 포함하여 압축
    -r 옵션이 없으면 해당 위치의 디렉토리는 압축되지만 디렉토리아의 파일들은 압축되지 않는다.
    -r [압축할 디렉토리]
-P
    압축 파일 생성 시 암호를 입력하여 생성
    -P [암호] (앞에 넣어야됨)
```
<br>


## 💡파일 풀기
### $ **unzip [압축 파일명.zip] [옵션]**
```
-d 
    지정된 위치에 압축 해제
    -d [저장할 경로]
```
<br>

## 💡python 코드로 압축 풀기
* extractall(path) : 경로에 있는 압축 파일 모두 풀기  
    path가 있으면 그 경로에 압축 풀기
``` python
import zipfile

# .zip 파일 풀기
with zipfile.ZipFile({압축 파일 경로}) as z:
    z.extractall({저장 경로})
```
<hr>
<br>

## 💡os 모듈 (import os)
#### 현재 경로 구하기
``` python
os.getcwd()
```
<br>

#### 하위의 폴더들을 for문으로 탐색
``` python
(root, dirs, files) = os.walks(path):
    '''
    root : dir과 files가 있는 path
    dirs : root아래에 있는 디렉토리 리스트
    files : root아래에 있는 파일 리스트

    topdown=True : 상위 디렉토리에서 최하위 디렉토리를 출력하는 top-down으로 탐색(default)
    topdown=False : 최하위 디렉토리에서 상위 디렉토리를 출력하는 bottom-up으로 탐색
    '''
```
<br>

#### 특정 경로에 존재하는 파일과 디렉토리 목록(리스트 타입)
``` python
os.listdir(path)
```
#### 특정 확장자만 출력(리스트 타입)
``` python
file_name = [_ for _ in os.listdir(path) if _.endswith('.확장명')]
```
<br>

#### 리눅스 명령어 실행
``` python
cmd_string = 'rm -r {}'.format(file_name)
os.system(cmd_string)
```
<br>

#### 해당 파일, 디렉토리가 존재하는 확인(boolean 타입)
`os.path.isdir`는 주어진 경로에 디렉토리가 존재하면 True를 return합니다. isdir은 symbolic link를 따라가므로 같은 path에 대해 islink()와 isdir() 모두 True를 return할 수도 있습니다

`os.path.exists`는 주어진 경로가 존재하면 `True`를 return합니다. 경로가 `broken symbolic link`인 경우에 `False`를 return하지요. 어떤 플랫폼에서는 경로가 존재하더라도 `os.stat()`으로 파일에 접근할 수 없는 경우에는 `False`를 return할 수 있습니다
``` python
os.path.exists(path) # 파일, 디렉토리 둘 다 확인
os.path.isfile(path)  # 파일이 존재하는지 확인
os.path.isdir(path)  # 디렉토리가 존재하는지 확인
```
<br>

#### 디렉토리 만들기
``` python
# exist_ok=True : 폴더가 존재하지 않으면 생성, 존재하는 경우에는 아무것도 하지 않는다.
# 에러 메세지도 표시하지 않습니다.
os.makedirs(path, exist_ok=True)  
```
<br>

#### path 형태로 합치기
```python
os.path.join(root_dir, file_name)

# ADD
'/'.join(list)
```

#### path에서 [:-1][:-1]를 split해주어서 dir, file를 나눠준다.
```
>>> os.path.split(r'c:\temp\test\python\hello.exe')
('c:\\temp\\test\\python', 'hello.exe')
파일부분과 폴더부분을 서로 잘라준다.
```

<hr><br>

## 💡glob 모듈 (import glob)
#### 해당 파일 가져오기
인자로 받은 패턴과 이름이 일치하는 모든 파일과 디렉토리의 리스트를 반환
```py
import glob
# from glob import glob (대중적)

patten = '~path~/*.확장자'
# patten = '~path~'
# patten = '~path~/file_name
glob(patten)
```
<hr><br>

## 💡shutil 모듈 (import shutil)
#### 파일 copy
```py
shutil.copy({복사할 파일}, {파일 저장 경로})

# ADD
!cp [복사할 파일] [파일 저장 경로]
```
<br>

#### 파일 move
```py
shutil.move({이동할 파일}, {파일 저장 경로})

# ADD
!mv [이동할 파일] [파일 저장 경로]
```

<hr><br>

## 💡cv2 모듈 (import cv2)
#### 이미지 읽기
```py
img = cv2.imread({이미지 경로})
```
<br>

#### 이미지 쓰기
```py
# {이미지}를 {이미지 경로}에 write
cv2.imwrite({이미지 경로/이미지이름}, {이미지})
```
<br>

#### 이미지 보기
```py
from google.colab.patches import cv2_imshow
cv2_imshow(cv2.imread({이미지 경로}))
```

## 💡PIL 모듈 (from PIL import Image)



<hr>
<br>

## 💡셀에서 출력 버리기
``` shell
[셀 명령어 or 출력 코드] > /dev/null
```
<hr>
<br>

## 💡bitbucket clone
``` python
import os
import urllib  # app password로 인코딩해준다.
from getpass import getpass  # 입력값을 password 타입으로 받음

user = input('User name: ')
password = getpass('Password: ')  # personal settings > App passwords
password = urllib.parse.quote(password) # your password is converted into url format
repo_name = input('Repo name: ')

cmd_string = 'git clone https://{0}:{1}@bitbucket.org/{2}.git'.format(user, password, repo_name)

os.system(cmd_string)
cmd_string, password = "", "" # removing the password from the variable
```

/root에 .git-credentials 파일을 올리고 나서 밑의 명령어를 통해 아이디와 패스워드를 저장
``` python
git config --global credential.helper store
```
``` bash
.git-cerdentials 파일 형식
https://{username}:{password}@bitbucket.org
https://{username}:{password}@gitlab.com
```
