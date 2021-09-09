'''입력'''
N = int(input())
ox_list = []
for i in range(N):
    ox_list.append((input()))

'''풀이1'''
# for i in range(N):
#     score = 0
#     plus_score = 0
#     for j in range(len(ox_list[i])):
#         if ox_list[i][j] == 'O':
#             plus_score += 1
#             score += plus_score
#         else:
#             plus_score = 0
#     print(score)

'''풀이2'''
for ox_str in ox_list: #ox_list에서 하나씩
    score = 0
    plus_score = 0
    for o_or_x in ox_str: #문자열 ox_str(ex.OOXXOXXOOO)에서 문자 하나씩
        if o_or_x == 'O':
            plus_score += 1
            score += plus_score
        else:
            plus_score = 0
    print(score)
