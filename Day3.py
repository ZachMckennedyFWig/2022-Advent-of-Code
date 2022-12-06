# Press the green button in the gutter to run the script.

def check(line):
    l = len(line) // 2
    left = line[:l]
    right = line[l:]

    for troll in range(l):
        for face in range(l):
            if left[troll] == right[face]:
                return left[troll]

def check2(one, two, three):
    o = len(one)
    clown = []

    for i in range(o):
        try:
            ind = two.index(one[i])
            if ind != -1:
                clown.append(two[ind])
        except:
            continue

    t = len(clown)

    for n in range(t):
        try:
            ind = three.index(clown[n])
            if ind != -1:
                return three[ind]
        except:
            continue


if __name__ == '__main__':
    file = open('Day3.txt')
    data = file.readlines()
    match = []
    count = 0


    while count < len(data) - 1:
        match.append(check2(data[count], data[count+1], data[count+2]))
        count = count + 3

    sum = 0

    for m in match:
        asc = ord(m)
        if asc > 96:
            sum = sum + asc - 96
        else:
            sum = sum + asc - 38

    print(sum)