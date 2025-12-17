print("\n+----------------- Task1 -----------------+")
my_friends = ["shakthi","peter","siva","saravanan","gomathi"]
print("My Friends:",end = " ")
for i in my_friends:
    print(i,end = " ")
my_friends.pop(4)
my_friends.append("Mathi")
print("\nThe updated friend List is: ",end = " ")
for i in my_friends:
    print(i,end = " ")
print("\n+-----------------------------------------+")


print("\n+----------------- Task2 -----------------+")
color_list = ["Red","Green","Yellow","Black","Blue","Pink"]
print("The First Three Colors Are: " , color_list[0:3])
print("The Last Two Are Colors: ", color_list[-2:])
print("+-----------------------------------------+")
