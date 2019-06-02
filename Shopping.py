print("Would you like to go shopping today?")

answer = input() 

if answer == "yes":
    print("What should we get?")
    list1 = input() 
    print("Great! We are going to get " + list1)
    print("Your list is ready to go")
    File_Object = open('shoppinglist.txt', 'w+')
    File_Object.writelines(list1) 
    File_Object.close()


if answer == "no":
    print("Maybe tomorrow")
