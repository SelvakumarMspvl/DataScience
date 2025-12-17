def calculateMean(List,length):
    sum = 0
    for i in List:
        sum += i
    avg = sum / length
    return avg


def calculateMedian(List, length, mid):
    sum = 0
    if mid % 2 == 0:
        for i in range(2):
            sum += List[(mid + i)-1]
        median = (sum / 2)
        return median

    else:
        return List[mid]

def Main():
    my_list = [230,450,120,370,500,280,190]

    my_list.sort()

    length = len(my_list)
    mid = length // 2

    avg = calculateMean(my_list,length)
    median = calculateMedian(my_list, length, mid)

    print("The Given List Is :", my_list)
    print("The Average Of The Given List IS: ",avg)
    print("The Median Of The Given List IS: ", median)

if __name__ == "__main__":
    Main()