# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('Day4.txt')
    data = file.readlines()

    count = 0

    for line in data:
        comma_split = line.split(',')
        left = comma_split[0].split('-')
        right = comma_split[1].split('-')

        if int(left[0]) <= int(right[0]) <= int(left[1]):
            count = count + 1
        elif int(left[0]) <= int(right[1]) <= int(left[1]):
            count = count + 1
        elif int(right[0]) <= int(left[0]) <= int(right[1]):
            count = count + 1
        elif int(right[0]) <= int(left[1]) <= int(right[1]):
            count = count + 1

    print(count)