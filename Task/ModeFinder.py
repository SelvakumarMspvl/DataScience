def max_value(List):
    value = List[0]
    for i in List:
        if value < i:
            value = i
    return value
def indexFinder(value,List):
    index = 0
    for i in range(len(List)-1):
        if value == List[index]:
            return index
        index += 1


def CountList(List):
    count = 0
    CountList =[]
    for i in List:
        for j in List:
            if i == j:
                count += 1
        CountList.append(count)
        count = 0
    return CountList


my_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
CountList = CountList(my_list)
max = max_value(CountList)
index = indexFinder(max,my_list)
print("The mode value is: ", my_list[index])