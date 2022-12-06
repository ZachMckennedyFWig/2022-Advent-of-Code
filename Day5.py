# Press the green button in the gutter to run the script.

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

if __name__ == '__main__':
    file = open('Day5.txt')
    data = file.readlines()

    count = 0
    stacks = {}

    while data[count][1] != '1':
        line = data[count]
        indeez = find(line, '[')

        for i in indeez:
            try:
                stacks[str(i//4+1)].append(line[i+1])
            except:
                stacks[str(i//4+1)] = [line[i+1]]

        count = count+1

    for line in data[count+2::]:
        splot = line.split(' ')
        n = int(splot[1])
        f = splot[3]
        t = splot[5][0]

        temp = stacks[f][0:n]
        temp.reverse()
        stacks[t] = temp + stacks[t]
        stacks[f] = stacks[f][n:]

    top = []

    for i in range(1, 10):
        top.append(stacks[str(i)][0])

    print(top)