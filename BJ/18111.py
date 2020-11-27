n, m, b = map(int, input().split())

ground = []
ground_times = dict()
time_by_dig = 2
time_by_put = 1

for i in range(n):
    ground += input().split()

for i in ground:
    if i not in ground_times:
        ground_times[i] = 1
    else:
        ground_times[i] += 1

'''
sorted_ground = sorted(ground_times.items(), key = lambda x : x[1])
choibin1 = sorted_ground[0][0]
choibin2 = sorted_ground[1][0]

def fix(choibin, b):
    global ground, time_by_put, time_by_dig

    fix_by_dig = 0
    fix_by_put = 0
    for i in ground:
        if i > choibin:
            fix_by_dig += 1
            b += 1
        elif i < choibin:
            if b > 0:
                fix_by_put += 1
                b -= 1
            else:
                return -1

    return fix_by_dig * time_by_dig + fix_by_put * time_by_put

result1 = fix(choibin1, b)
result2 = fix(choibin2, b)

if result1 < result2:
    print(result1, choibin1)
else:
    print(result2, choibin2)
'''