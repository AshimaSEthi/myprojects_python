import datetime

user_name = input("Enter your Name: ")
print("Hello",str(user_name),"!!!")
today = datetime.date.today()
todo_list = input("Please enter todo list for {} using commas: ".format(today))
filename = "Todo List - "+str(today)+".txt"

l1 = todo_list.split(',')

with open(filename,'w+') as f:
    f.write("To DO List for Today ({}):\n\n".format(today))
    for number,letter in enumerate(l1,1):
        listt = str(number)+' '+str(letter)
        f.write(listt)
        f.write("\n")

