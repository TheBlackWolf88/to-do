import math
import os
import getpass
import time
import json
user = getpass.getuser()

def loald():
    try:
        with open('todo.txt',"r")as f:
            data = json.loads(f.read())
        return data
    except FileNotFoundError:
        list=[]
        with open('todo.txt','w') as f:
            json.dump(list,f)
        return list
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def save(todo):
    list = loald()
    list.append(todo)
    with open('todo.txt', 'w') as txt_file:
        json.dump(list, txt_file)
def load():
    list = loald()
    for i in list:
        print("-"+i[0].upper()+i[1:])
def header(): 
    print("-----------------------------------")
    print(user.upper()+"\'S TO-DO LIST") 
    print("-----------------------------------")


def rm(index):
    list=loald()
    list.pop(int(index))
    with open('todo.txt','w') as f:
        json.dump(list, f)
while True:
    clear()
    header()
    load()
    print("-----------------------------------")
    str=input("Enter a new to-do or type C to exit. To remove an item use rm: ")
    if str.lower()=="c":
        exit()
    elif str.startswith("rm"):
        try:
            index = str[3:]
            rm(index)
        except ValueError:
            try:
                 if index=="a":
                    list = []
                    with open('todo.txt', 'w') as file:
                        json.dump(list,file)
                 else:
                    x = input("Type C to cancel, A to clear all the todos or specify which todo you want to complete: ")
                    x=x.lower()
                    if x=="c":
                        pass
                    elif x=="a":
                        list = []
                        with open('todo.txt', 'w') as file:
                            json.dump(list,file)
                    else:
                        rm(x)
            except IndexError:
                clear()
                list=loald()
                print("You entered an invalid number. The maximum number is", len(list)-1)
                time.sleep(2)
            except:
                clear()
                print("An error has occured. Returning..")
                time.sleep(2)
                pass
        except IndexError:
            clear()
            list = loald()
            print("You entered an invalid number. The maximum number is ",len(list)-1)
            time.sleep(2)
        except:
            clear()
            print("An error has occured. Returning..")
            time.sleep(2)
    else:
        save(str)
