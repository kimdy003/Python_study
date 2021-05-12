import matplotlib.pyplot as plt
from wordcloud import WordCloud


#전처리
def get_except_keyword(filename):
    keyword_list = list()
    with open(filename, encoding='utf-8') as f:
        for keyword in f.readlines():
            keyword_list.append(keyword.strip())
    return keyword_list

kko = open("./word/KakaoTalkChats_hansung.txt", "r", encoding='UTF8')
out = open("./word/kakao.txt", "w", encoding='UTF8')

#특정 단어 필터링
except_word = get_except_keyword('./word/except_word.txt')
while True:
    line = kko.readline()
    for Str in except_word:
        line = line.replace(Str, '')
    if not line: break
    idx = 0
    for i, v in enumerate(line):
        if v == ":":
            idx = i
    set_line = line[idx+2:]
    if set_line != '\n':
        out.write(line[idx+2:])
    
kko = open("./word/kakao.txt", "r", encoding='UTF8').read()

wc = WordCloud(font_path='./word/font/NanumGothic.ttf', background_color='white', 
    width=800, height=600).generate(kko)

plt.figure(figsize=(20, 20)) #이미지 사이즈 지정
plt.imshow(wc, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거
plt.show() 
plt.savefig()
