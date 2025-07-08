import sys as s
stack=[]
def insert_beg():
    n=int(input("Enter the Elemnent"))
    stack.insert(0,n)
def delete_beg():
    stack.pop(0)
def exit_program():
    s.exit("End of program")

menu = {
    1: insert_beg,
    2:delete_beg,
    3:exit_program
}

while True:
    print("1. insert at beg 2. delete from beg 3. exit")
    choice = int(input("Enter a choice: "))
    menu.get(choice)