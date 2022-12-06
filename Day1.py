# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('Day1.txt')
    data = file.readlines()

    print(data)

    temp = 0
    temp_ind = []
    biggest = []

    for i, v in enumerate(data):
        try:
            temp = temp + int(v[:-1])
            temp_ind.append(i)
        except:
            biggest.append(temp)
            temp = 0
            continue

    biggest.sort(reverse=True)
    summy = 0

    for j in range(3):
        summy = summy+biggest.pop(0)


    print(summy)


