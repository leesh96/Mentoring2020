import sys

N, M = map(int, sys.stdin.readline().split())
word = []
word1 = []
word2 = []
word3 = []

#입력
array = []
for _ in range(N):
    array.append(sys.stdin.readline().strip())

#가로단어
for w in array:
    word1.extend(w.split('#')) #샵기준으로 나누기

for i in range(len(word1)): #두글자 이상인 단어만 word에 추가
    if len(word1[i]) > 1:
        word.append(word1[i])

#세로단어
for i in range(M): #세로인 단어만들기(샵포함)
    temp = ''
    for j in range(N):
            temp = temp + array[j][i]
    word2.append(temp)

for w in word2: #샵기준으로 나누기
    word3.extend(w.split('#'))

for i in range(len(word3)): #두글자 이상인 단어만 word에 추가
    if len(word3[i]) > 1:
        word.append(word3[i])

#정렬
word.sort()
print(word[0])
