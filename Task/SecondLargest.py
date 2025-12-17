def Sort(my_list):
    length = len(my_list)
    for i in range(length):
        for j in range(length):
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list

def LengthFinder(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count

List = [1,2,5,4,8,56,4,78,79]
print("The given List Is: ",List)
List = Sort(List)
print("The Second Largest Number In The List Is: ",List[1])