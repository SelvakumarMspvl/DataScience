Str = input("Enter The Sentance With Delimiter: ")
temp = ""
index = 0
for i in range(len(Str)):
    if index < len(Str):
        if Str[index].isalpha():
            temp += Str[index]
        else:
            temp += Str[index+1].capitalize()
            index += 1
        index += 1

print(Str,"  -->  ",temp )