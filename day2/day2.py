with open('day2/day2.txt') as file:
    lines = file.readlines()

    score = 0
    for line in lines:
        value = line.strip().split(' ')
        him = value[0]
        you = value[1]

        print(score)
        if him == 'A':
            if you == 'X':
                score += 3
            if you == 'Y':
                score += 4
            if you == 'Z':
                score += 8
        if him == 'B':
            if you == 'X':
                score += 1
            if you == 'Y':
                score += 5
            if you == 'Z':
                score += 9
        if him == 'C':
            if you == 'X':
                score += 2
            if you == 'Y':
                score += 6
            if you == 'Z':
                score += 7

    print(score)