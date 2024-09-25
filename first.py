# Ctrl + Shift + F5 --> To run program

print ('My first Python program')

name = "Vijay" #input ("Enter your name : ")
print ("Hello " + name)

def myFun():
    print ("Program started")

def add_2_numbers(a, b):
    # print (a + b)
    return a+b

if __name__ == "__main__":
    myFun()

    print(add_2_numbers(3,4))

    print ("nothing")