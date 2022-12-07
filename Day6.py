# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('Day6.txt')
    data = file.readlines()

    line = data[0]

    unique_len = 14

    count = 0
    test = line[unique_len:]

    while True:
        zeezer = {}
        for i in range(unique_len):
            zeezer[str(line[count+i])] = 0
        if len(list(zeezer.keys())) == unique_len:
            break
        count = count+1

    print(count + unique_len)