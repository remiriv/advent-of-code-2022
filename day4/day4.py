with open('day4/day4.txt') as file:
    lines = [line.strip().split(',') for line in file]
    result = 0
    for line in lines:
        min1, max1 = line[0].split("-")
        min2, max2 = line[1].split('-')
        if (int(min1) <= int(min2) <= int(max1)) or (int(min2) <= int(min1) <= int(max2)):
            result += 1

    print(result)
'''
    for line in lines:
        min1, max1 = line[0].split("-")
        min2, max2 = line[1].split('-')
        if (int(min1) <= int(min2) and int(max1) >= int(max2)) or (int(min2) <= int(min1) and int(max2) >= int(max1)):
            result += 1

    print(result)
'''
