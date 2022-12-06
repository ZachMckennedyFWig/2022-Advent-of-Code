# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('Day2.txt')
    data = file.readlines()

    temp = ['X', 'Y', 'Z', 'X', 'Z']
    map = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    score = 0

    for line in data:
        bonobo = map[line[0]]
        indeez = temp.index(bonobo)

        if line[2] == 'X':
            ruhehehehe = temp[indeez-1]
        elif line[2] == 'Y':
            ruhehehehe = temp[indeez]
        else:
            ruhehehehe = temp[indeez+1]

        addy = temp.index(ruhehehehe)+1

        if ruhehehehe == temp[indeez]:
            score = score + addy + 3
        elif ruhehehehe == temp[indeez + 1]:
            score = score + addy + 6
        else:
            score = score + addy

    print(score)