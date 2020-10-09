'''입력'''
input_list = list(map(int, input().split()))
'''풀이'''
std_list = [1, 2, 3, 4, 5, 6, 7, 8]
std_reverse_list = list(reversed(std_list))

if std_list == input_list:
    print("ascending")
elif std_reverse_list == input_list:
    print("descending")
else:
    print("mixed")