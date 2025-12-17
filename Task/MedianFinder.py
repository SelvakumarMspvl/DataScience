def Sort(my_list):
    length = LengthFinder(my_list)
    for i in range(length):
        for j in range(length):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list

def LengthFinder(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count


def medianFinder(mid,my_list):
    sum = 0
    if mid % 2 == 0:


        for i in range(2):
            sum += my_list[(mid + i) - 1]
        avg = sum / 2
        print("Median is: ", avg)
    else:
        print("Median is: ", my_list[mid -1])

def Main():
    my_list = [8,7,6,5,4,3,2]
    length =  LengthFinder(my_list)
    Sort(my_list)

    print(my_list)
    mid = length // 2

    medianFinder(mid,my_list)

if __name__ == "__main__":
    Main()